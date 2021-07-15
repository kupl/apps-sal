a, b = input().split()

if int(a) + int(b) < 24:
    print(int(a) + int(b))
elif int(a) + int(b) >= 24:
    print(int(a) + int(b) - 24)
