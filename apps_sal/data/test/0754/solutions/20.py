n = int(input())
t = input()
s, x = 0, t[0]
for i in range(1, n):
    if t[i] == x:
        s += 1
    else:
        x = t[i]
print(s)

