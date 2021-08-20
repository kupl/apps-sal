q = int(input())
ls = [True] * (10 ** 5 + 1)
(ls[0], ls[1]) = (False, False)
for i in range(2, 10 ** 5 + 1):
    if ls[i]:
        for j in range(i * 2, 10 ** 5 + 1, i):
            ls[j] = False
ps = [0] * (10 ** 5 + 1)
for i in range(10 ** 5):
    ps[i + 1] = ps[i]
    if ls[i + 1] == True and ls[(i + 2) // 2] == True and ((i + 1) % 2 == 1):
        ps[i + 1] += 1
for _ in range(q):
    (l, r) = list(map(int, input().split()))
    print(ps[r] - ps[l - 1])
