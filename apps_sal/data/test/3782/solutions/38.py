n, k, q = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 10**9
for i in a:
    A = []
    l = []
    ln = 0
    for j in a + [-1]:
        if i > j:
            if ln - k + 1 >= 0:
                l.sort()
                A += l[:ln - k + 1]
            l = []
            ln = 0
        else:
            l.append(j)
            ln += 1
    if len(A) < q:
        continue
    else:
        A.sort()
        ans = min(ans, A[q - 1] - i)
print(ans)
