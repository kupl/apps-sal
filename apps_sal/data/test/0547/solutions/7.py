n, k = (int(_) for _ in input().split())
a = []
for i in range(n):
    a.append(input())
pw = input()
x, y = 0, 0
for s in a:
    if s == pw:
        continue
    if len(s) < len(pw):
        x += 1
        y += 1
    if len(s) == len(pw):
        y += 1
x += (x // k) * 5
y += (y // k) * 5
print(x + 1, y + 1)
