(n, q) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort(reverse=True)
p = []
p.append(l[0])
for i in l[1:]:
    p.append(p[-1] + i)


def bs(l, c):
    i = 0
    j = len(l) - 1
    ans = -1
    while i <= j:
        mid = i + (j - i) // 2
        if l[mid] >= c:
            ans = mid
            i = mid + 1
        else:
            j = mid - 1
    return ans


for _ in range(q):
    x = int(input())
    x = bs(l, 2 * x)
    if x == -1:
        print(0)
    else:
        print(p[x])
