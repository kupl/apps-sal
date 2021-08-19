3.5
n = int(input())
A = [int(s) for s in input().split(' ') if s != '']
B = [(x, i) for (i, x) in enumerate(A)]
B.sort()
_sum = sum(A)
L = []
for (i, (x, j)) in enumerate(B):
    __sum = _sum - x
    if i == len(A) - 1:
        _max = B[-2][0]
    else:
        _max = B[-1][0]
    __sum -= _max
    if __sum == _max:
        L.append(j + 1)
print(len(L))
if len(L) != 0:
    for i in range(0, len(L) - 1):
        print(L[i], end=' ')
    print(L[-1])
