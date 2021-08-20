n = int(input())
t = list(map(int, input().split()))
tmp = [0] * n
cnt1 = 1
cnt2 = 0


def counting_sort(array, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array


if max(t) > 500000:
    t.sort()
else:
    t = counting_sort(t, max(t))


def foo(x, n):
    tmp = [0] * n
    cnt2 = 1
    for i in range(1, n):
        tmp[i] = sum(x[:i])
        if tmp[i] <= x[i]:
            cnt2 += 1
    return cnt2


'\nfor i in range(1,n):\n    tmp[i] = sum(t[:i])\n    if tmp[i]<=t[i]:\n        cnt1+=1\n'
'for i in range(1,n):\n    tmp[i] = sum(x[:i])\n    if tmp[i]<=x[i]:\n        cnt2+=1\n    else:\n        if len(x[i:])>=len(x[:i]):\n            if x[i]<=x[i-1]:\n                print(len(x[i-1:]))\n                quit()\nprint(cnt2)'
c = 0
for i in range(n):
    if t[i] >= c:
        cnt2 += 1
        c += t[i]
    'tmp[i] = sum(t[:i])\n    if tmp[i]<=t[i]:\n        cnt2+=1\n    else:\n        t[i] = 0'
print(cnt2)
