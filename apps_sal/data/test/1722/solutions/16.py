n = int(input())
l = [0] * 26
for _ in range(n):
    s = input()
    l[ord(s[0]) - 97] += 1
ans = 0
for i in range(26):
    x = l[i] // 2
    y = l[i] - x
    ans += x * (x - 1) // 2
    ans += y * (y - 1) // 2
print(ans)
