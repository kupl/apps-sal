input()
c = [int(a) for a in input().split()]
a = [int(a) for a in input().split()]
count = 0
for i in c:
    if len(a) > 0 and i <= a[0]:
        count += 1
        a.pop(0)
print(count)
