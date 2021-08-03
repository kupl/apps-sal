n, k = list(map(int, input().split()))
aa = sorted(map(int, input().split()))

answ = 0

for a in aa:
    while 2 * k < a:
        k *= 2
        answ += 1
    k = max(k, a)

print(answ)
