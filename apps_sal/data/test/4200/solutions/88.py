def iparse():
    return list(map(int, input().split()))


n, m = iparse()
a = iparse()
s = sum(a)
k = (s + 4 * m - 1) // (4 * m)
cnt = 0
for e in a:
    if e >= k:
        cnt += 1
print("Yes" if cnt >= m else "No")
