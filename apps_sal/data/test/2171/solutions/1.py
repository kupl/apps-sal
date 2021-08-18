try:
    n = int(input())
    a = n % 6
    if a == 0 or a == 1 or a == 3:
        print("yes")
    else:
        print("no")
except:
    pass
