N = int(input())
lsa = list(map(int, input().split()))
ls = [0] * (N + 1)
for i in range(N, 0, -1):
    k = 0
    c = 2 * i
    while c <= N:
        k += ls[c]
        c += i
    if k % 2 == lsa[i - 1] % 2:
        continue
    ls[i] = 1
ls.pop(0)
M = ls.count(1)
print(M)
if M != 0:
    ls1 = []
    for i in range(N):
        if ls[i] == 1:
            ls1.append(i + 1)
    ls2 = [str(i) for i in ls1]
    print(' '.join(ls2))
