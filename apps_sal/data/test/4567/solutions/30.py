arr = []
arr2 = []
for i in range(int(input())):
    a = int(input())
    if a % 10 == 0:
        arr2.append(a)
    else:
        arr.append(a)
arr.sort()
j = sum(arr) + sum(arr2)
if j % 10 != 0:
    print(j)
else:
    k = 0
    while j % 10 == 0 and k < len(arr):
        j -= arr[k]
        k += 1
    if j % 10 == 0:
        print(0)
    else:
        print(j)
