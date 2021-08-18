
import sys

[n, k1, k2] = list(map(int, sys.stdin.readline().strip().split()))
ais = list(map(int, sys.stdin.readline().strip().split()))
bis = list(map(int, sys.stdin.readline().strip().split()))

k = k1 + k2
cis = [abs(ai - bi) for ai, bi in zip(ais, bis)]
cis.sort(reverse=True)
cis.append(0)

s = 0
i = 1
done = False
while i < n + 1:
    s += i * (cis[i - 1] - cis[i])
    if s >= k:
        done = True
        break
    i += 1

if not done:
    if (k - s) % 2 == 0:
        print(0)
    else:
        print(1)
else:
    d = s - k
    h = d // i
    n1 = d % i
    n0 = i - n1
    print(sum(ci**2 for ci in cis[i:]) + n0 * (cis[i] + h)**2 + n1 * (cis[i] + h + 1)**2)
