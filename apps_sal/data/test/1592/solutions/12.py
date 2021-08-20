(Messages, Max, Last) = (0, 0, 0)
for i in range(int(input())):
    X = list(map(int, input().split()))
    Messages = max(0, Messages - (X[0] - Last))
    Messages += X[1]
    Max = max(Messages, Max)
    Last = X[0]
print(Last + Messages, Max)
