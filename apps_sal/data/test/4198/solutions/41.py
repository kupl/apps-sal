A, B, X = list(map(int, input().split()))
good = 0
bad = 10 ** 9 + 1
while bad - good > 1:
    mid = (bad + good) // 2
    if A * mid + B * len(str(mid)) <= X:
        good = mid
    else:
        bad = mid
print(good)
