n = int(input())
c = 0
for _ in range(n):
    (a, b) = map(int, input().split())
    if a == b:
        c += 1
    if a != b:
        c = 0
    if c == 3:
        print('Yes')
        break
if c < 3:
    print('No')
