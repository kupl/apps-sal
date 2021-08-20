from itertools import product
(n, m) = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
bit = [1, -1]
su_max = 0
for i in product(bit, repeat=3):
    l_1 = []
    for (a, b, c) in l:
        t = a * i[0] + b * i[1] + c * i[2]
        l_1.append(t)
    l_1 = sorted(l_1)[::-1]
    su_max = max(su_max, sum(l_1[:m]))
print(su_max)
