(a, b) = list(map(int, input().split()))
cnt = 0
for i in range(a, b + 1):
    l = []
    while i > 0:
        l.append(i % 10)
        i //= 10
    if l[0] == l[4] and l[1] == l[3]:
        cnt += 1
print(cnt)
