import itertools
def F(s):
    a = ''
    for i in s:
        a += i * 2
    return int(a)
n = int(input())
a = input().split()
print((sum(list(map(F, a))) * n) % 998244353)

