n = int(input())
A = [int(i) for i in input().split()]

ans = []
_max = max(A)
_min = min(A)
_min_ptr = A.index(_min)
_max_ptr = A.index(_max)
if _min == _max:
    print((0))
    return

if sorted(A) == A:
    print((0))
    return

if _max < 0:
    for i in range(n - 1, 0, -1):
        A[i - 1] += A[i]
        ans.append((i, i - 1))

elif _min >= 0:
    for i in range(0, n - 1):
        A[i + 1] += A[i]
        ans.append((i, i + 1))

elif _min < 0 and _max >= 0 and abs(_min) > abs(_max):
    for i in range(n):
        if A[i] >= 0:
            A[i] += _min
            ans.append((_min_ptr, i))
    for i in range(n - 1, 0, -1):
        A[i - 1] += A[i]
        ans.append((i, i - 1))

elif _min < 0 and _max >= 4 and abs(_min) <= abs(_max):
    for i in range(n):
        if A[i] < 0:
            A[i] += _max
            ans.append((_max_ptr, i))
    for i in range(0, n - 1):
        A[i + 1] += A[i]
        ans.append((i, i + 1))


if len(ans) == 0:
    print((0))
    return

print((len(ans)))
for i, j in ans:
    print((i + 1, j + 1))

