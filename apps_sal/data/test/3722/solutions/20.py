(N,) = list(map(int, input().split()))
X = dict()
X['AA'] = input().strip()
X['AB'] = input().strip()
X['BA'] = input().strip()
X['BB'] = input().strip()
ss = set(['AB'])
R = [1]
for i in range(4):
    nss = set()
    for t in ss:
        for j in range(i + 1):
            nt = t[:j + 1] + X[t[j:j + 2]] + t[j + 1:]
            nss.add(nt)
    ss = nss
    R.append(len(ss))
MOD = 10 ** 9 + 7
if N - 2 < 5:
    print(R[N - 2])
elif R[-3] + R[-2] == R[-1]:
    for _ in range(N - 2 - 4):
        R.append((R[-1] + R[-2]) % MOD)
    print(R[-1])
elif R[-2] == R[-1]:
    print(R[-1])
elif R[-2] * 2 == R[-1]:
    for _ in range(N - 2 - 4):
        R.append(R[-1] * 2 % MOD)
    print(R[-1])
