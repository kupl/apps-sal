x = input().split()
n = int(x[0])
if x[2] == "week":
    if n == 5 or n == 6:
        print(53)
    else:
        print(52)
else:
    if n < 30:
        print(12)
    elif n == 30:
        print(11)
    else:
        print(7)
