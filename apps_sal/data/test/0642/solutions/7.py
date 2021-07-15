n, m = list(map(int, input().split()))

if m == 0:
    ok = True
else:
    hole = sorted(map(int, input().split()))
    ok = hole[0] != 1 and hole[-1] != n
    for i in range(2, m):
        if hole[i] == hole[i-1]+1 == hole[i-2]+2:
            ok = False
            break

print("YES" if ok else "NO")



