import math
N = int(input())

ans = ""
if N == 1:
    print("1")
elif N == 0:
    print("0")
elif N == -1:
    print("10")
else:
    while True:
        r = N % 2
        N = (N - r) / -2
        ans = str(int(r)) + ans
        if N == 0 or N == 1:
            ans = str(int(N)) + ans
            break

    print(ans)
