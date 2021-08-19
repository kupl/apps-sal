n, s = list(map(int, input().split()))

allCups = list(map(int, input().split()))
sumK = sum(allCups)
minK = min(allCups)
if sumK < s:
    print(-1)

else:
    if sumK - (minK * n) >= s:
        print(minK)
    else:
        s = s - (sumK - (minK * n))
        # print(s)
        if s % n == 0:
            print(minK - (s // n))
        else:
            print(minK - (s // n) - 1)
