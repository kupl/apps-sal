(n, s) = list(map(int, input().split()))
allCups = list(map(int, input().split()))
sumK = sum(allCups)
minK = min(allCups)
if sumK < s:
    print(-1)
elif sumK - minK * n >= s:
    print(minK)
else:
    s = s - (sumK - minK * n)
    if s % n == 0:
        print(minK - s // n)
    else:
        print(minK - s // n - 1)
