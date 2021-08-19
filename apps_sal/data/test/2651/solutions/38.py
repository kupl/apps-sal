n, m = map(int, input().split())
X = sorted([int(x) for x in input().split()])
Y = sorted([int(x) for x in input().split()])
mod = 1000000007


def diffSum(X):  # Σ(X[j]-X[i]) 1<=i<j<=N
    l = len(X)
    Res = [(2 * i - l + 1) * X[i] for i in range(l)]
    return sum(Res) % mod


print(diffSum(X) * diffSum(Y) % mod)
