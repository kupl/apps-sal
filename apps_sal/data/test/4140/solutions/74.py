s = [int(x) for x in list(input())]
x = len(s)
y = [0 if i % 2 == 0 else 1 for i in range(x)]
z = [1 if i % 2 == 0 else 0 for i in range(x)]
count1 = 0
count2 = 0
ans1 = list(zip(s, y))
ans2 = list(zip(s, z))
for a in ans1:
    if a[0] != a[1]:
        count1 += 1
for a in ans2:
    if a[0] != a[1]:
        count2 += 1
print(min(count1, count2))
