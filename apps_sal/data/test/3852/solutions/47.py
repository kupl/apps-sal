def inpl():
    return list(map(int, input().split()))


N = int(input())
a = inpl()
ans = []
c = []
(l, r) = (0, N - 1)
while l < r:
    if a[l] <= 0:
        c.append((0, l))
        l += 1
        continue
    elif a[r] >= 0:
        c.append((1, r))
        r -= 1
        continue
    elif a[l] + a[r] <= 0:
        c.append((0, l))
        ans.append((r + 1, l + 1))
        l += 1
    else:
        c.append((1, r))
        ans.append((l + 1, r + 1))
        r -= 1
for (s, b) in c[::-1]:
    if s == 0:
        ans.append((b + 2, b + 1))
    else:
        ans.append((b, b + 1))
print(len(ans))
for (x, y) in ans:
    print(x, y)
