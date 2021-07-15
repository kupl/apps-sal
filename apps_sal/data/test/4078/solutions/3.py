n, m = map(int, input().split())
arr = [int(x) for x in input().split()]
seg = []
el = []
el2 = []
h = []

def cont(a, b, c):
    return a <= c <= b

def count_delta():
    return max(h) - min(h)

def decrement(l, r):
    for i in range(l - 1, r):
        h[i] -= 1

for i in range(m):
    seg.append([int(x) for x in input().split()])

for i in range(len(arr)):
    h = arr[:]
    tmp = []
    for j in range(len(seg)):
        if cont(seg[j][0], seg[j][1], i + 1):
            decrement(seg[j][0], seg[j][1])
            tmp.append(j + 1)
    el.append(count_delta())
    el2.append(tmp)
    
print(max(el))
k = el.index(max(el))
print(len(el2[k]))
print(*el2[k])
