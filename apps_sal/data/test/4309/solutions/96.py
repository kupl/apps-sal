n = input()
k = int(n) % 111
if k == 0:
    print(n)
else:
    if n[0] > n[1] or (n[0] == n[1] and n[1] > n[2]):
        print(n[0] * 3)
    else:
        print((str(int(n[0]) + 1)) * 3)
