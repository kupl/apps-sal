N = int(input())
A = [[] * N for _ in range(N)]
for i in range(N):
    a = int(input())
    for _ in range(a):
        x, y = [int(x) for x in input().split()]
        A[i].append([x - 1, y])

ans = 0
for i in range(1, 1 << N):
    B = format(i, f'0{N}b')[::-1]
    possible = True
    cnt = 0
    for j in range(N):
        if B[j] == '1':
            cnt += 1
            for v in A[j]:
                if v[1] != int(B[v[0]]):
                    possible = False
                    break
    if possible:
        ans = max(ans, cnt)
print(ans)

