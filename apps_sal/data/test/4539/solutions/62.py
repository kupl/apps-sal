n = input()
d = sum(list(map(int, n)))

if int(n) % d == 0:
    print("Yes")
else:
    print("No")
