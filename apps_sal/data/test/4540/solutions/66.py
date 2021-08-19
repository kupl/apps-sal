n = int(input())
As = list(map(int, input().split()))
ais = [0]
ais.extend(As)
m = 0
ais.append(m)
S = 0
for i in range(n - 1):
    S += abs(As[i] - As[i + 1])
S += abs(As[0]) + abs(As[n - 1])
for i in range(1, n + 1):
    sb1 = abs(ais[i - 1] - ais[i])
    sb2 = abs(ais[i] - ais[i + 1])
    ad = abs(ais[i - 1] - ais[i + 1])
    ans = S - sb1 - sb2 + ad
    print(ans)
