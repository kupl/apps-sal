N, M, X = list(map(int, input().split()))
S = list(map(int, input().split()))
Fees = list(S)
Goal1 = []
Goal2 = []
count1 = 0
count2 = 0
point0 = 0

for i in range(X):
    point0 += 1
    Goal1.append(point0)

for j in range(N - X):
    X += 1
    Goal2.append(X)

for fee in Fees:
    if fee in Goal1:
        count1 += 1
    if fee in Goal2:
        count2 += 1

if count1 >= count2:
    print(count2)
if count1 < count2:
    print(count1)
