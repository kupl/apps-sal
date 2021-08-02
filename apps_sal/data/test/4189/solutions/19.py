a = int(input())
s, h = 0, 0
for i in range(a):
    q = input()
    if (q.split()[-1] == "soft"):
        s += 1
    else:
        h += 1
m = max(s, h)
q = 1
while (1):
    if ((q * q + 1) // 2 >= m):
        if (q * q < s + h):
            q += 1
        print(q)
        break
    q += 1
