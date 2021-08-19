def f(a, b):
    val = 0
    for x in range(a, b):
        for y in range(x + 1, b):
            if ar[x] > ar[y]:
                val += 1
    return val


n = int(input())
ar = list(map(int, input().split()))
inv = f(0, n)
m = int(input())
ans = []
for x in range(m):
    (l, r) = map(int, input().split())
    z = r - l + 1
    inv += int(z * (z - 1) / 2)
    inv %= 2
    ans.append('odd' if inv else 'even')
print(*ans, sep='\n')
