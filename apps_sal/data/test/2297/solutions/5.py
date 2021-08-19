q = int(input())
for i in range(q):
    (l, r) = map(int, input().split())
    if l % 2 == 0:
        count = -((r - l + 1) // 2)
    else:
        count = (r - l + 1) // 2
    if (r - l + 1) % 2 == 0:
        print(count)
    elif r % 2 == 0:
        print(count + r)
    else:
        print(count - r)
