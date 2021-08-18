n = int(input())
A = list(map(int, input().split()))
A.sort()
multiple = [0] * (A[-1] + 1)
for i in range(n):
    now = A[i]
    while(now <= A[-1]):
        multiple[now] += 1
        now += A[i]
ans = 0
for i in range(n):
    if(multiple[A[i]] == 1):
        ans += 1
print(ans)
