N, K = list(map(int, input().split()))


def Aoki(x, K):
    x = abs(x - K)
    return x


if N % K == 0:
    ans = 0
    print(ans)
    return
lis = []
lis.append(N)
x = N % K
for i in range(10000):
    lis.append(x)
    x = Aoki(x, K)
print((min(lis)))
