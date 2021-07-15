n, m, k = list(map(int, input().split()))
a, b = list(map(int, input().split()))
podE = a // (m * k)
if a % (m * k) != 0:
    podE += 1
podN = b // (m * k)
if b % (m * k) != 0:
    podN += 1
etE = (a % (m * k)) // k
if (a % (m * k)) % k != 0:
    etE += 1
etN = (b % (m * k)) // k
if (b % (m * k)) % k != 0:
    etN += 1
if podE == 0:
    podE = n
if etE == 0:
    etE = m
if podN == 0:
    podN = n
if etN == 0:
    etN = m

if podE == podN and etE == etN:
    print(0)
elif podE == podN:
    print(min(abs(etE - etN) * 5, 10 + abs(etE - etN)))
else:
    down = min((etE - 1) * 5, 10 + (etE - 1))
    move = min(abs(podE - podN), (n - max(podN, podE)) + min(podE, podN)) * 15
    up = min((etN - 1) * 5, 10 + (etN - 1))
    print(down + move + up)

