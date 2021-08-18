n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
s = 0
for i in range(n):
    s += abs(l[i] - l[n // 2])
if s <= k:
    print(0)
else:
    i = 0
    while True:
        if i == n - 1:
            break
        if l[i + 1] != l[i]:
            break
        i += 1
    p = i
    left = p + 1
    i = n - 1
    while True:
        if i == 0:
            break
        if l[i - 1] != l[i]:
            break
        i -= 1
    kon = i
    right = n - kon
    while True:
        if left <= right:
            if k >= left * (l[p + 1] - l[p]):
                k -= left * (l[p + 1] - l[p])
                while True:
                    p += 1
                    left += 1
                    if p >= n:
                        break
                    if l[p + 1] != l[p]:
                        break
            else:
                print(l[kon] - l[p] - k // left)
                break
        else:
            if k >= right * (l[kon] - l[kon - 1]):
                k -= right * (l[kon] - l[kon - 1])
                while True:
                    kon -= 1
                    right += 1
                    if kon == 0:
                        break
                    if l[kon] != l[kon - 1]:
                        break
            else:
                print(l[kon] - l[p] - k // right)
                break
