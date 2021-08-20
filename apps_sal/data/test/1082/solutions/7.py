n = int(input())
s = []
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
for k in set(map(int, input().split())):
    d = 0
    for q in p:
        while k % q == 0:
            k //= q
            d ^= 1 << q
    for j in s:
        d = min(d, d ^ j)
    if d:
        s.append(d)
print(pow(2, n - len(s), 1000000007) - 1)
