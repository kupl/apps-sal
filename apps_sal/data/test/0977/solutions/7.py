(n, p) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = []
for x in range(1, 2001):
    fail = 0
    pointer = 0
    for i in range(n):
        while pointer < n - 1 and x + i - a[pointer + 1] >= 0:
            pointer += 1
        if (pointer + 1 - i) % p == 0:
            fail = 1
            break
        if x + i - a[pointer] < 0:
            fail = 1
            break
    if fail == 0:
        ans.append(str(x))
print(len(ans))
print(' '.join(ans))
