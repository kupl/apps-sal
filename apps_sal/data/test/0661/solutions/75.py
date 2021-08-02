m, k = map(int, input().split())
if k >= 2 ** m:
    print(-1)
    return
if m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    if k == 1:
        print(-1)
    return
base = [i for i in range(2**m) if i != k]
ans = base + [k] + base[::-1] + [k]
print(*ans)
