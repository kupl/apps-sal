n = int(input())
line_a = list(map(int, input().split()))
m = int(input())
line_b = list(map(int, input().split()))
if sum(line_a) != sum(line_b):
    print(-1)
else:
    sa = 0
    sb = 0
    l = 0
    r = 0
    size = 0
    while l != n and r != m:
        if sa + line_a[l] > sb + line_b[r]:
            sb += line_b[r]
            r += 1
        elif sa + line_a[l] < sb + line_b[r]:
            sa += line_a[l]
            l += 1
        elif sa + line_a[l] == sb + line_b[r]:
            size += 1
            l += 1
            r += 1
            sa = 0
            sb = 0
    print(size)
