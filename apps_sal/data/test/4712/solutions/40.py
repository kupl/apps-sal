H, W = list(map(int, input().split()))
res = []

for i in range(H + 2):
    if i == 0 or i == H + 1:
        l = '#' * (W + 2)
        res.append(l)
    else:
        a = input()
        a = '#' + a + '#'
        res.append(a)

for i in res:
    print(i)
