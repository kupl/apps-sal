a = list(map(int, input().split()))
s = input()
ans = 0
for item in s:
    ans += a[int(item) - 1]
print(ans)
