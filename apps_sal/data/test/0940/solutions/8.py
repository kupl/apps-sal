arr = list(map(int, input().split()))
maxval = max(arr)
if sum(arr) - maxval > maxval:
    print(0)
else:
    val1 = sum(arr) - maxval
    print(maxval + 1 - val1)
