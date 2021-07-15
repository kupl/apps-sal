n = int(input())
if n > 81:
    print("No")
else:
    for i in range(9):
        if n % (i+1) == 0 and 1 <= n/(i+1) <= 9:
            print("Yes")
            return
    print("No")

