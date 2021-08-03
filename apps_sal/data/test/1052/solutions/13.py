n = [int(i) for i in input().split()]
if n[1] == 1:
    print("1")
elif n[1] == 2:
    print(int(((n[0] * (n[0] - 1)) / 2) + 1))
elif n[1] == 3:
    print(int(((n[0] * (n[0] - 1)) / 2) + 1 + n[0] * (n[0] - 1) * (n[0] - 2) / 3))
elif n[1] == 4:
    print(int(((n[0] * (n[0] - 1)) / 2) + 1 + n[0] * (n[0] - 1) * (n[0] - 2) / 3 + (3 / 8) * n[0] * (n[0] - 1) * (n[0] - 2) * (n[0] - 3)))
