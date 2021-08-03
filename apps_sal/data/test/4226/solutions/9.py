a, b = input().split(" ")

ans = 0
for i in range(int(a) + 1):
    turu = int(i)
    turt = int(a) - int(i)

    if turu * 2 + turt * 4 == int(b):
        ans = 1
        break

if ans == 1:
    print("Yes")
else:
    print("No")
