N = int(input())
if N % 1000 == 0:
    print(0)
else:
    n = str(N)
    print(1000 - int(n[-3:]))
