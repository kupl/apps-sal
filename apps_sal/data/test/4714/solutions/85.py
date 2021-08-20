(a, b) = list(map(int, input().split()))
cnt = 0
l = []
newl = []
for i in range(a, b + 1):
    l = []
    while i > 0:
        l.append(i % 10)
        i //= 10
    newl = l[::-1]
    if l == newl:
        cnt += 1
print(cnt)
