t = list(map(int, input().split()))
x = min(t)
s = 0
for i in range(3):
    s += (t[i] - x) // 3
    if (t[i] - x) % 3 == 2 and x > 0:
        s += 1
        t[i] = x - 1
    else:
        t[i] = x + (t[i] - x) % 3
print(s + min(t))
