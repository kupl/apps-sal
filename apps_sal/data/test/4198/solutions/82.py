A, B, X = map(int, input().split())
left, right = 0, int(X / A)
while (right - left) > 1:
    mid = int((left + right) / 2)
    if (mid * A) + (len(str(mid)) * B) <= X:
        left = mid
    else:
        right = mid
if left <= X:
    if left >= 10**9:
        print(10**9)
    else:
        print(left)
else:
    print(0)
