n, m = list(map(int, input().split()))
ls = []
for i in range(1, int(m**(1 / 2)) + 1):
    if m % i == 0:
        ls.append(i)
        ls.append(m // i)
ls = sorted(list(set(ls)), reverse=True)
for j in ls:
    if j * n <= m:
        print(j)
        break
