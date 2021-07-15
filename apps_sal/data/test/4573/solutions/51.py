N = int(input())
X = list(map(int, input().split()))
med1 = sorted(X)[N // 2 - 1]
med2 = sorted(X)[N // 2]
for i in range(N):
    tmp = X[i]
    if tmp <= med1:
        print(med2)
    else:
        print(med1)

