m, n = list(map(int, input().split()))
t = []

for i in range(m):
    temp = list(map(int, input().split()))
    bit = 0
    for i in temp[1:]:
        bit ^= (1 << (i - 1))
    t.append(bit)

ans = True

for i in range(m - 1):
    for j in range(i + 1, m):
        if t[i] & t[j] == 0:
            ans = False

print('possible' if ans else 'impossible')
