v = int(input())
a = list(map(int, input().split()))
(index, val) = (-1, 10 ** 12)
for i in range(len(a)):
    if a[i] <= val:
        val = a[i]
        index = i
m = v // val
ans = [str(index + 1) for x in range(m)]
if not len(set(a)) == 1:
    left = v - m * val
    for i in range(len(ans)):
        potential = left + val
        for (j, k) in enumerate(reversed(a)):
            if k <= potential:
                left = potential - k
                ans[i] = str(9 - j)
                break
print(''.join(ans) if ans else -1)
