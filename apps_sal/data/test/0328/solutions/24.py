n = int(input())
ans = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if a + b > ans:
        ans = a + b
print(ans)
