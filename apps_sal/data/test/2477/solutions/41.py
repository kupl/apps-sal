N, K = map(int, input().split())
A = list(map(int, input().split()))


def f(n):
    now = 0
    for i in range(N):
        now += (A[i] - 1) // x
    if now <= K:
        return True
    else:
        return False


l = 0; r = 10**10
while r - l > 1:
    x = (l + r) // 2
    if f(x):
        r = x
    else:
        l = x
print(r)
