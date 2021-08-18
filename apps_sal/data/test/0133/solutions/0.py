
def rint():
    return int(input())


def rints():
    return list(map(int, input().split()))


M = 10**9 + 7
n, m = rints()
print(pow((pow(2, m, M) + M - 1) % M, n, M))
