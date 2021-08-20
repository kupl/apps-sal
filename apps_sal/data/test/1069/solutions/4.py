N = input()
X = 0
if len(N) > 2:
    X = int(N[-2:])
else:
    X = int(N)
if X % 4 == 0:
    print(4)
else:
    print(0)
