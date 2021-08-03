n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort(reverse=True)
j = -1
for i in range(len(a)):
    if a[i] == 0:
        j += 1
        a[i] = b[j]
        if j == len(b):
            break
flag = 0
for i in range(len(a) - 1):
    if a[i] >= a[i + 1]:
        flag = 1
        break
if flag == 1:
    print("Yes")
else:
    print("No")
