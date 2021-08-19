(N, K) = map(int, input().split())
list = [0] * (N + 1)
mod = 10 ** 9 + 7
list[1] = 1
list[0] = 1
for i in range(1, N):
    list[i + 1] = list[i] * (i + 1) % mod


def c(a, b):
    ans = list[a] * pow(list[b], mod - 2, mod) * pow(list[a - b], mod - 2, mod) % mod
    return ans


for i in range(1, K + 1):
    if i > N - K + 1:
        print(0)
    else:
        an = c(K - 1, i - 1) * c(N - K + 1, i) % mod
        print(an)
