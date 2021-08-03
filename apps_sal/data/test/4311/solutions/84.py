s = int(input())
l = [s]
a = set(l)
for i in range(10**6):
    if l[-1] % 2 == 0:
        n = l[-1] // 2
    else:
        n = 3 * l[-1] + 1
    if n not in a:
        a.add(n)
        l.append(n)
    else:
        print(len(l) + 1)
        break
