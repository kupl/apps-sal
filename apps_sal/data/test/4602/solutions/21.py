n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for i in x:
    ans += min(i, k - i)
print(2 * ans)
