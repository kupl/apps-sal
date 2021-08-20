N = int(input())
A = [0] + [int(input()) for _ in range(N)]
j = 1
cnt = 0
check = False
for i in range(N):
    if j == 2:
        check = True
        break
    cnt += 1
    j = A[j]
print(cnt if check else -1)
