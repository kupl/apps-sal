n, m = list(map(int, input().split()))
A = [list(input()) for _ in range(n)]
B = [list(input()) for _ in range(m)]
ok = False
for ai in range(n-m+1):
    for aj in range(n-m+1):
        match = True
        for bi in range(m):
            for bj in range(m):
                b = B[bi][bj]
                a = A[ai+bi][aj+bj]
                if a == b:
                    continue
                else:
                    match = False
                    break
            if not match:
                break
        else:
            ok = True
        if ok:
            break
    if ok:
        break
print(('Yes' if ok else 'No'))

