(N, K) = map(int, input().split())
A = list(map(int, input().split()))


def f(x):
    if x != 0:
        now = 0
        for i in range(N):
            now += (A[i] - 1) // x
        return now <= K
    else:
        return False


l = 0
r = 10 ** 10
while r - l > 1:
    x = (l + r) // 2
    if f(x):
        r = x
    else:
        l = x
print(r)
