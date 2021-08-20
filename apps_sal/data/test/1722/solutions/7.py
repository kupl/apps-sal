n = int(input())
s = [input() for i in range(n)]
ans = 0
for c_i in range(26):
    c = chr(ord('a') + c_i)
    cnt = sum((1 for name in s if name.startswith(c)))
    a = cnt // 2
    b = cnt - a
    ans += a * (a - 1) // 2
    ans += b * (b - 1) // 2
print(ans)
