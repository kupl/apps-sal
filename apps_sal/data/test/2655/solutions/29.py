N = int(input())
A = [int(_) for _ in input().split()]

A.sort(reverse=True)

ans = 0
for i in range(N-1):
    ans += A[(i+1) // 2]
print(ans)

