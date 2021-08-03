from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


n, m = nii()


def divisore(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort(reverse=True)
    return divisors


d = divisore(m)

for x in d:
    zan = m - (x * n)
    if zan >= 0 and zan % x == 0:
        print(x)
        return
