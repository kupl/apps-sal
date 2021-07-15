n = int(input())

l = []
for _ in range(n):
    l.append(int(input()))

l.sort()
m = sum(l)

if m % 10 != 0:
    print(m)
else:
    for e in l:
        if (m - e) % 10 != 0:
            print((m-e))
            return

    print((0))

