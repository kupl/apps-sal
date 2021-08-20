(n, k) = list(map(int, input().split()))
a = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]
a.sort()
f.sort(reverse=True)


def score(x):
    syugyo = 0
    for (A, F) in zip(a, f):
        sup = x // F
        if sup < A:
            syugyo += A - sup
    if syugyo <= k:
        return True
    return False


left = 0
right = a[-1] * f[0] + 1
while left < right - 1:
    mid = (left + right) // 2
    if score(mid):
        right = mid
    else:
        left = mid
print(left + 1 if left != 0 else 0)
