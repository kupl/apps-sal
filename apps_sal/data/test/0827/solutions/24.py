import sys
sys.setrecursionlimit(700000)


def s_in():
    return input()


def n_in():
    return int(input())


def l_in():
    return list(map(int, input().split()))


n = n_in()
s = s_in()

N = 3 * (10**10)
t = '110' * 2 * n

res = 0

if s == "0":
    print((10**10))
    return

if s == "1":
    print((2 * 10**10))
    return

if s == "10":
    print((10**10))
    return

if s == "11":
    print((10**10))
    return

if s == "00":
    print((0))
    return

if s == "01":
    print((10**10 - 1))
    return


if s == t[:n]:
    res += (N - n) // 3 + 1
if s == t[1:n + 1]:
    res += (N - n - 1) // 3 + 1
if s == t[2:n + 2]:
    res += (N - n - 2) // 3 + 1

print(res)
