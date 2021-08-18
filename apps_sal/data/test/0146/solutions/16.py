from operator import itemgetter
n, k = list(map(int, input().split()))
ar = list(map(int, input().split()))
e = 0
s = 0
ans = 0
for j in range(k):
    e = 0
    s = 0
    for i in range(n):
        if i % k == j:
            continue
        if ar[i] == 1:
            e += 1
        else:
            s += 1
    ans = max(ans, abs(e - s))
print(ans)
