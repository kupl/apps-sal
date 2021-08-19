N = int(input())
count = [0] * (N + 1)
modz = 10 ** 9 + 7


def junretsu(a):
    if a <= 0:
        return 1
    if a & 1 == 1:
        return 2 * junretsu(a - 1) % modz
    else:
        rr = junretsu(a >> 1)
        return rr * rr % modz


pos = list(map(int, input().split()))
for i in range(N):
    count[pos[i]] += 1
diff = [0] * (N + 1)
for i in range(1, N + 1):
    d = abs(N - i - (i - 1))
    diff[d] += 1
invalid = False
total = 1
for i in range(N):
    if count[i] != diff[i]:
        invalid = True
        break
if invalid:
    print(0)
else:
    print(junretsu(int(N / 2)))
