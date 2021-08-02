

isp = [True] * (10**6 + 8)
isp[0] = isp[1] = False

i = 2
N = 10**6 + 7
while i * i <= N:
    if isp[i]:
        for j in range(i * i, N + 1, i):
            isp[j] = False
    i += 1
n = int(input())
for m in range(1, 1001):
    if not isp[n * m + 1]:
        print(m)
        break
