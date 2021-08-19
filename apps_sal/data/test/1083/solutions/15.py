n = int(input())
a = [int(i) for i in range(1, n + 1)]
a.reverse()
left = 0
right = 0
l = []
r = []
for i in a:
    if left < right:
        left += i
        l.append(i)
    else:
        right += i
        r.append(i)
print(abs(left - right))
l.sort()
r.sort()
ans = [l, r]
ans.sort()
print(len(ans[0]), ' '.join((str(i) for i in ans[0])))
