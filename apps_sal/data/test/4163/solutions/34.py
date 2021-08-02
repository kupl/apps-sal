n = int(input())

ctn_check = 0
for _ in range(n):
    d1, d2 = input().split()
    if d1 == d2:
        ctn_check += 1
    else:
        ctn_check = 0
    if ctn_check == 3:
        break

if ctn_check == 3:
    print("Yes")
else:
    print("No")
