(n, k) = map(int, input().split())
a = list(map(int, input().split()))
answ = 0
for b in range(n):
    sm = 0
    for i in range(n):
        if (i - b) % k:
            sm += a[i]
    answ = max(answ, abs(sm))
print(answ)
