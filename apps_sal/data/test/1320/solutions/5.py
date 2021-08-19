n = int(input())
pole = []
ans = 0
for i in range(n):
    s = input()
    h = 0
    for j in s:
        if j == 'C':
            h += 1
    ans += h * (h - 1) // 2
    pole.append(s)
for i in range(n):
    h = 0
    for j in range(n):
        if pole[j][i] == 'C':
            h += 1
    ans += h * (h - 1) // 2
print(ans)
