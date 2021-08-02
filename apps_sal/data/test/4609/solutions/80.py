N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()

i = 0
ans = 0
while i < N:
    tmp = A[i]
    count = 0
    while i < N and A[i] == tmp:
        count += 1
        i += 1
    ans += count % 2

print(ans)
