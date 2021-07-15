modulo = 998244353

def conv(x):
    res = 0
    for v in x:
        res = (res * 100 + int(v)) % modulo
    return res

n = int(input())
print(sum(map(conv, input().split())) * n * 11 % modulo)
