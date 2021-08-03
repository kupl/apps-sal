n = int(input())
s = input()
x = 0
res = 0

for i in range(n):
    if s[i] == "I":
        x += 1
    else:
        x -= 1
    res = max(res, x)

print(res)
