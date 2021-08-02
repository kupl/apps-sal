N = int(input())
X = list(map(int, input().split()))
_min = min(X)
_max = max(X)
_sum = 1000000000
for i in range(_min, _max + 1):
    temp = 0
    for x in X:
        temp += (x - i) * (x - i)
    if temp < _sum:
        _sum = temp
print(_sum)
