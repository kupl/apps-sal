def dist(a, f, i):
    for j in range(i + 1, len(a)):
        if f == a[j]:
            return j


(n, k) = map(int, input().split())
a = list(map(int, input().split()))
books = set()
l = 0
pref = [0 for i in range(n)]
for i in range(n - 1, -1, -1):
    pref[a[i] - 1] = max(pref[a[i] - 1], i)
res = 0
for i in range(n):
    if a[i] not in books:
        if l == k:
            for j in books:
                if pref[j - 1] < i:
                    l -= 1
                    books.discard(j)
                    break
            if l == k:
                m = -1
                for j in books:
                    if dist(a, j, i) > m:
                        m = dist(a, j, i)
                        ind = j
                books.discard(ind)
                l -= 1
        res += 1
        books.add(a[i])
        l += 1
print(res)
