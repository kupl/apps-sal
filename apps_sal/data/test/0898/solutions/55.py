(n, m) = map(int, input().split())
li = []
for i in range(int(m ** 0.5) + 1, 0, -1):
    if i == int(m ** 0.5) + 1 and (i - 1) ** 2 == m:
        continue
    if m % i == 0:
        li.append(i)
        li.append(m // i)
li.sort(reverse=True)
for i in li:
    if n <= m // i:
        print(i)
        break
