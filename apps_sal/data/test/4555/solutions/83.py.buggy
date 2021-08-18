a, b, k = map(int, input().split())
li = []
if (b - a) + 1 < k or (b - a) < k * 2:
    for i in range(a, b + 1):
        li.append(i)
    for i in li:
        print(i)
    return
for i in range(a, a + k):
    li.append(i)
for i in range(b - k + 1, b + 1):
    li.append(i)
for i in li:
    print(i)
