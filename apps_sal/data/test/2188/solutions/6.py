n = int(input())
l1 = []
l2 = []
for i in range(n):
    (a, b) = map(int, input().split())
    if a < b:
        l1.append((a, b, i + 1))
    else:
        l2.append((b, a, i + 1))
l1.sort()
l1 = l1[::-1]
l2.sort()
if len(l1) >= len(l2):
    print(len(l1))
    for item in l1:
        print(item[2], end=' ')
else:
    print(len(l2))
    for item in l2:
        print(item[2], end=' ')
