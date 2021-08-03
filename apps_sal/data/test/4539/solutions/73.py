N = input()
fX = sum([int(i) for i in list(N)])
X = int(N)
if X % fX == 0:
    print("Yes")
else:
    print("No")
