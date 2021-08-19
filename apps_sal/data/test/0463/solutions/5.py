(n, x) = list(map(int, input().split()))
a = set((int(i) for i in input().split()))
if len(a) != n:
    ans = 0
else:
    shift = set()
    ans = -1
    for i in a:
        shift.add(i & x)
        if i & x != i and i & x in a:
            ans = 1
    if len(shift) != n and ans == -1:
        ans = 2
print(ans)
