n = int(input())
A = sorted(list(map(int, input().split())))
cnt = 0
for i in range(n):
    cnt += abs(A[i] - (i + 1))
print(cnt)
