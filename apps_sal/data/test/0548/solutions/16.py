n = int(input())
a = list(map(int, input().split()))
isodd = False
if sum(a) % 2 == 1:
    print("First")
    return
for i in range(n):
    isodd = isodd or (a[i] % 2 == 1)
if isodd:
    print("First")
else:
    print("Second")
