s = [0]
for i in range(1, 2000):
    s.append(s[-1] + i)

a, b = int(input()), int(input())
x = abs(a - b)

print(s[x // 2] + s[x - x // 2])
