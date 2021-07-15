n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(k):
    t1, t2 = 0, 0
    for j in range(i, n, k):
        if a[j] == 1:
            t1 += 1
        else:
            t2 += 1
    ans += min(t1, t2)
print(ans)

