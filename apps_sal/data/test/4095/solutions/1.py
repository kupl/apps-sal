n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
diff = [0] * n
for i in range(n):
    if a[i] < m:
        diff[i] = -1
    if a[i] > m:
        diff[i] = 1

aim = a.index(m)
left = {}
right = {}
suml = 0
for i in reversed(list(range(aim + 1))):
    suml += diff[i]
    if not suml in left:
        left[suml] = 0
    left[suml] += 1

sumr = 0
for i in range(aim, n):
    sumr += diff[i]
    if not sumr in right:
        right[sumr] = 0
    right[sumr] += 1

# print(left)
# print(right)

ans = 0
for i in left:
    wk1 = -i
    if wk1 in right:
        ans += left[i] * right[wk1]
    wk1 = 1 - i
    if wk1 in right:
        ans += left[i] * right[wk1]

print(ans)
