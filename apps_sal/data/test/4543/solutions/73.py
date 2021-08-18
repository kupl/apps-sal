e1, e2 = list(map(str, input().split()))
count = 0
a = e1 + e2
for i in range(1, int(a)):
    if int(a) / int(i) == int(i):
        count += 1
if count > 0:
    print('Yes')
else:
    print('No')
