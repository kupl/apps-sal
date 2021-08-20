(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10 ** 9 + 7


def count(li):
    l = 1 - len(li)
    cnt = 0
    for (ind, i) in enumerate(li):
        cnt += i * (l + 2 * ind)
    return cnt % mod


print(count(x) * count(y) % mod)
