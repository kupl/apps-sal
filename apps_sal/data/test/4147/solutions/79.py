from itertools import product
p = 4
n, a, b, c = map(int, input().split())
banboo = [0] * n
for i in range(n):
    banboo[i] = int(input())

Bit_4 = list(product(range(p), repeat=n))
ans = 10**6
for Bi in Bit_4:
    tmp = [0] * 4
    magic = 0
    if 1 in Bi and 2 in Bi and 3 in Bi:
        for i in range(n):
            tmp[Bi[i]] += banboo[i]
            if tmp[Bi[i]] != banboo[i] and Bi[i] != 0:
                magic += 10
        magic += abs(tmp[1] - a)
        magic += abs(tmp[2] - b)
        magic += abs(tmp[3] - c)
        ans = min(magic, ans)
print(ans)
