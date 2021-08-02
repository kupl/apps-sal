s = input()
N = int(s)
Sn = sum([int(i) for i in list(s)])
if N % Sn == 0:
    print("Yes")
else:
    print("No")
