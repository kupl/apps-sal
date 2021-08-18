def printAns(first, start, end, s):
    cnt = end - start + 1
    loop = (N - start - 1) // cnt
    add = N - (cnt * loop) - start
    print((s[end] - s[start - 1]) * loop + s[start - 1 + add])


N, X, M = map(int, input().split())

check = [0] * M
m = [X]
a = X

for i in range(1, N):
    a = (a**2) % M
    if check[a - 1] != 0:
        printAns(0, check[a - 1], i - 1, m)
        return
    elif a == 0:
        print(m[i - 1])
        return
    check[a - 1] = i
    m.append(m[-1] + a)
else:
    print(m[-1])
