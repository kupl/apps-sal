n = int(input())
lst = list(map(int, input().split()))
a = list()
count = 0
for i in range(n):
    if lst[i] % 2 == 0:
        a.append(lst[i])
for i in range(len(a)):
    if a[i] % 3 == 0 or a[i] % 5 == 0:
        count += 1
if count == len(a):
    print('APPROVED')
else:
    print('DENIED')
