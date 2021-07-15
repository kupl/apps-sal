n = int(input())
a = [int(x) for x in input().split()]
summ = 0
count = 0
minn = 10000000000000
for i in range(n):
    if a[i] % 2 == 1:
        minn = min(minn, a[i])
        count += 1
if count % 2 == 0:
    print(sum(a))
else:
    print(sum(a) - minn)
