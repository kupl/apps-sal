n = int(input())
a = list(map(int, input().split()))
stairs = [1] * n
(l, r) = (10 ** 9, -2 ** 5)
for i in range(n):
    stairs[i] += i
    r = max(r, a[i] - stairs[i])
    l = min(l, a[i] - stairs[i])


def pos(b):
    return sum((abs(i - b - j) for (i, j) in zip(a, stairs)))


while l + 2 < r:
    c1 = l + (r - l) // 3
    c2 = r - (r - l) // 3
    if pos(c1) < pos(c2):
        r = c2
    else:
        l = c1
ans = min(min(pos(l), pos(r)), pos(l + 1))
print(ans)
