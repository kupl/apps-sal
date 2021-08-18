s = input().strip()
n = s.count('n')
e = s.count('e') // 3
i = s.count('i')
t = s.count('t')


count = min(e, i, t)
for i in range(count, -1, -1):
    if (2 * i + 1) <= n:
        print(i)
        break
    elif 3 * i <= n:
        print(i)
        break
