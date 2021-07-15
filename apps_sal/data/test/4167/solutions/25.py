n, k = map(int, input().split())
candidOdd = 0
candidEven = 0
candidEven2 = 0
for i in range(1, n+1):
    if k % 2 == 1:
        if i % k == 0:
            candidOdd += 1
    else:
        if i % k == 0:
            candidEven += 1
        elif i % k == (k/2):
            candidEven2 += 1
print(candidOdd**3 + candidEven**3 + candidEven2**3)
