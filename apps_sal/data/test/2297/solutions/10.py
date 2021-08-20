cs = int(input())
for c in range(cs):
    (l, r) = map(int, input().split())
    if l % 2 == 0 and r % 2 == 0:
        print((r - l) // 2 + l)
    if l % 2 == 1 and r % 2 == 0:
        print((r - l + 1) // 2)
    if l % 2 == 0 and r % 2 == 1:
        print(-(r - l + 1) // 2)
    if l % 2 == 1 and r % 2 == 1:
        print(-(r - l) // 2 - l)
