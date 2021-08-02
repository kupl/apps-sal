s = int(input())

if (s == 0):
    print("1")
if (s % 4 == 0 and s != 0):
    print("6")
if (s % 4 == 1):
    print("8")
if (s % 4 == 2):
    print("4")
if (s % 4 == 3):
    print("2")
