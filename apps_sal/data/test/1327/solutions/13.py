N, M = map(int, input().split())
l = []
for i in range(N):
    l.append(list(map(int, input().split())))

ans = 0
for i in range(2**3):
    bs = format(i, "03b")
    lsum = []
    for j in range(N):
        lsum.append(sum([l[j][_] * (2 * int(bs[_]) - 1) for _ in range(3)]))
    lsum.sort(reverse=True)
    ans = max(ans, sum(lsum[:M]))
print(ans)
