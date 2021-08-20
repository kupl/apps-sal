(p, q, l, r) = map(int, input().split())
mySet1 = set()
mySet2 = set()
for i in range(p):
    (a, b) = map(int, input().split())
    for i in range(a, b + 1):
        mySet1.add(i)
for i in range(q):
    (a, b) = map(int, input().split())
    for i in range(a, b + 1):
        mySet2.add(i)
m = max(mySet1)
cnt = 0
for t in range(l, r + 1):
    for item in mySet2:
        if t + item in mySet1:
            cnt += 1
            break
print(cnt)
