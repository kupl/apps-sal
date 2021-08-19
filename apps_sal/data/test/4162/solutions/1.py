n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += i - 1
print(ans)
