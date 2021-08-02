n = int(input())
l1 = [0] * 26
for i in range(n):
    s = input()
    l1[ord(s[0]) - 97] += 1
ans = 0
for item in l1:
    x = item // 2
    y = item - x
    ans += x * (x - 1) // 2
    ans += y * (y - 1) // 2
print(ans)
