def gns():
    return list(map(int, input().split()))


n = int(input())
ns = input().split()


def db(x):
    ans = ''
    for c in x:
        ans += c * 2
    return ans


md = 998244353
ns = [int(db(x)) % md for x in ns]
sm = sum(ns)
print(sm * n % md)
