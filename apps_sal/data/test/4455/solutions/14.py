from collections import Counter


def binary(x, ar):
    low = 0
    high = len(ar) - 1
    while low <= high:
        mid = (low + high) // 2
        if ar[mid] == x:
            break
        elif ar[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return mid


(n, q) = list(map(int, input().split()))
l = list(map(int, input().split()))
frq = dict(Counter(l))
new = sorted(set(l))
look = [frq[new[0]]]
for i in range(1, len(new)):
    look.append(look[i - 1] + frq[new[i]])
d = dict()
for i in range(q):
    (li, r) = list(map(int, input().split()))
    li -= 1
    r -= 1
    if li in d:
        d[li].append(r)
    else:
        d[li] = [r]
    if r in d:
        d[r].append(li)
    else:
        d[r] = [li]
enum = []
for i in range(n):
    x = binary(l[i], new)
    if x == 0:
        sum1 = 0
    else:
        sum1 = look[x - 1]
        if i in d:
            for j in range(len(d[i])):
                if l[d[i][j]] < l[i]:
                    sum1 -= 1
    enum.append(sum1)
print(*enum)
