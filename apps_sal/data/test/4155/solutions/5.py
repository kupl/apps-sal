n = int(input())
h = list(map(int, input().split()))
cnt = 0
for i in range(n):
    while h[i] != 0:
        cnt += 1
        for j in range(i, n):
            if h[j] != 0:
                h[j] = h[j] - 1
            elif h[j] == 0:
                break
print(cnt)
