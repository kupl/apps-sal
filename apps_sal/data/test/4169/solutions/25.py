n, m = map(int, input().split())
k = [list(map(int, input().split())) for _ in range(n)]

sum = 0
mr = 0
ks = sorted(k)

for i in range(n):
    if ks[i][1] < (m - mr):
        sum += ks[i][0] * ks[i][1]
        mr += ks[i][1]

    else:
        sum += ks[i][0] * (m - mr)
        break

print(sum)
