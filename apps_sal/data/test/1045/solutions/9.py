n = int(input())
t, s, i = 0, 0, 0
while s <= n:
    i += 1
    t += i
    s += t

print(i - 1)
