(n, k, q) = map(int, input().split())
A = list(map(int, input().split()))
ans = 10 ** 18
for x in A:
    B = []
    C = []
    for a in A:
        if a >= x:
            C.append(a)
        else:
            if len(C) >= k:
                C.sort()
                B += C[0:len(C) - k + 1]
            C = []
    else:
        if len(C) >= k:
            C.sort()
            B += C[0:len(C) - k + 1]
    if len(B) >= q:
        B.sort()
        ans = min(ans, B[q - 1] - x)
print(ans)
