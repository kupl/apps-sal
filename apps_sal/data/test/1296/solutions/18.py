def newArr(a, k):
    b = a
    i = 0
    n = len(a)
    while i < n:
        b[i] += (i+1)*k
        i += 1
    return b

def minSum(a, k):
    a.sort()
    sm = 0
    cnt = 0
    i = 0
    while i < k:
        sm += a[i]
        i += 1
    return sm


inp = input().split()
n = int(inp[0])
S = int(inp[1])
inp = input().split()
a = []
for x in inp:
    a.append(int(x))
l = 0
r = n
while l<r:
    mid = (l+r)//2
    if l+1 == r:
        mid = r
    b = newArr(list(a), mid)
    if minSum(b, mid) <= S:
        l = mid
    else:
        r = mid - 1
ans = l
print(str(ans) + ' ' + str( minSum(newArr(a, ans), ans) ))

