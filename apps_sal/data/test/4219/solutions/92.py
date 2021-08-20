import itertools
n = int(input())
tes = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        (x, y) = list(map(int, input().split()))
        tes[i].append([x - 1, y])
ans = 0
for tf_s in itertools.product(list(range(2)), repeat=n):
    for i in range(n):
        if tf_s[i] == 0:
            continue
        for (x, y) in tes[i]:
            if tf_s[x] != y:
                break
        else:
            continue
        break
    else:
        ans = max(ans, tf_s.count(1))
print(ans)
