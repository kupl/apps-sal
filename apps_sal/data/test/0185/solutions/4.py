n, k = list(map(int, input().split()))

if k == 1:
    print(3 * (n - 1) + 3)
elif k == n:
    print(3 * (n - 1) + 3)

else:
    shorter = min(k - 1, n - k)
    longer = max(k - 1, n - k)
    out = 0
    out += shorter * 3 + shorter + longer * 3 + 3
    print(out)
