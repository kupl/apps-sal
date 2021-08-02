n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
S = 0
_min = b[0] // a[0]
for i in range(n):
    S += a[i]
    x = b[i] // a[i]
    if x < _min:
        _min = x
for i in range(n):
    b[i] -= a[i] * _min
cnt = _min
while True:
    need = S
    for i in range(n):
        if b[i] < a[i]:
            need -= b[i]
            b[i] = 0
        else:
            need -= a[i]
            b[i] -= a[i]
    if need < k:
        k -= need
        cnt += 1
    elif need == k:
        cnt += 1
        break
    else:
        break
print(cnt)
