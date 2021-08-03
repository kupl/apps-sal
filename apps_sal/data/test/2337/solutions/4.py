n, m = map(int, input().split())
treb = list(map(int, input().split()))
est = list(map(int, input().split()))
c = [0 for i in range(max(treb[-1], est[-1]) + 1)]
for i in range(n):
    c[treb[i] - 1] += 1
i = m - 1
e = n
q = treb[-1]
while i != -1:
    d = True
    for j in range(min(est[i] - 1, q), -1, -1):
        if c[j] > 0:
            q = j
            c[j] -= 1
            d = False
            e -= 1
            break
    if d:
        print(e)
        return
    i -= 1
print(e)
