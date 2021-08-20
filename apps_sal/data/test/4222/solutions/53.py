def N():
    return int(input())


def L():
    return list(map(int, input().split()))


def NL(n):
    return [list(map(int, input().split())) for i in range(n)]


mod = pow(10, 9) + 7
(n, k) = L()
l = [1] * n
for i in range(k):
    d = N()
    a = L()
    for j in a:
        l[j - 1] = 0
print(l.count(1))
