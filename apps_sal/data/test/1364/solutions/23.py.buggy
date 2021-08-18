n = int(input())
a = list(map(int, input().split()))

box = []
num = a[0]
count = 1
for i in range(1, n):
    if a[i] == num:
        count += 1
    else:
        num = a[i]
        box.append(count)
        count = 1
box.append(count)

if len(box) == 1:
    print(0)
    return

ans = 0
for x, y in zip(box, box[1:]):
    ans = max(ans, min(x, y))

print(ans * 2)
