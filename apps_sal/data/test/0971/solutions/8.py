n, lim, d = map(int, input().split())
q = list(map(int, input().split()))
cur = 0
counter = 0
for elem in q:
    if elem > lim:
        continue
    cur += elem
    if cur > d:
        counter += 1
        cur = 0
print(counter)
