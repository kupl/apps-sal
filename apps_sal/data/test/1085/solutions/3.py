from sys import stdin


def nii():
    return map(int, stdin.readline().split())


def lnii():
    return list(map(int, stdin.readline().split()))


n = int(input())


def divisore(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


ans_l = divisore(n - 1)[1:]
d = divisore(n)
for i in d[1:]:
    nn = n
    while nn % i == 0:
        nn //= i
    if nn % i == 1:
        ans_l.append(i)
print(len(ans_l))
