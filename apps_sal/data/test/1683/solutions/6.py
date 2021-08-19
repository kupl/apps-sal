from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
A = list(input().split())
mod = 998244353


def calc(a, k):
    a0 = a[-k:]
    a1 = a[:-k]
    A1 = 0

    if a1 != "":
        A1 = int(a1) * (10**(k * 2)) * 2

    ANS = ""
    for k in a0:
        ANS += k * 2

    return A1 + int(ANS)


L = [len(a) for a in A]


C = Counter(L)
ANS = 0

for a in A:
    # LEN_a=len(a)

    for k in range(1, 11):
        x = C[k]
        # if k==LEN_a:
        #    x-=1

        ANS = (ANS + calc(a, k) * x) % mod

print(ANS)
