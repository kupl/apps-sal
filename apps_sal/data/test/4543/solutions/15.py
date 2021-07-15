a, b = input().split()
x = int(a+b)
no = 0
for i in range(1000):
    if x == i**2:
        print("Yes")
    else:
        no += 1
        if no == 1000:
            print("No")
