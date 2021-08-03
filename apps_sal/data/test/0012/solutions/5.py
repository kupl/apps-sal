n = int(input())
s = input()
g1 = 0
g2 = 0
ans = 0
num2 = s.count("G")
for i in range(n):
    if s[i] == "G":
        g1 += 1
    else:
        g2 = g1
        g1 = 0

    num = g1 + g2
    if num2 != num:
        num += 1
    ans = max(ans, num)
print(min(n, ans))
