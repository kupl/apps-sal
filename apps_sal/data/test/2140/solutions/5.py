s = list(input())
m = int(input())
a = list(map(int, input().split()))
swap = False
a.sort()
(i, j) = (0, 0)
for i in range(len(s) // 2):
    while j < m and a[j] - 1 <= i:
        swap = not swap
        j += 1
    if swap:
        (s[i], s[len(s) - i - 1]) = (s[len(s) - i - 1], s[i])
print(''.join(s))
