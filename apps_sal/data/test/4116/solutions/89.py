n = int(input())
flag = 0
for i in range(1, 10):
    if n % i == 0:
        tar = n // i
        if tar > 0 and tar < 10:
            flag = 1
if flag == 0:
    print("No")
else:
    print("Yes")
