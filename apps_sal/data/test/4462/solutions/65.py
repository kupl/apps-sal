n = int(input())
a = list(map(int, input().split()))
a4 = []
a2 = []
a1 = []
for i in range(n):
    if a[i] % 4 == 0:
        a4.append(a[i])
    elif a[i] % 2 == 0:
        a2.append(a[i])
    else:
        a1.append(a[i])
if len(a4) >= n//2:
    print("Yes")
elif len(a4) + len(a2)//2 >= n//2:
    print("Yes")
else:
    print("No")
