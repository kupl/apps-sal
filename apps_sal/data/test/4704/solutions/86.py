n = int(input())
a = list(map(int, input().split()))
s = sum(a)
temp, ans = 0, float('inf')
for v in a[:-1]:
    temp += v
    s -= v
    ans = min(ans, abs(temp - s))
print(ans)
