A = sorted(map(int, input().split()))
count_odds = 0
for a in A:
    if a & 1:
        count_odds += 1
if count_odds == 0 or count_odds == 3:
    print(((A[2] * 2 - A[0] - A[1]) // 2))
elif count_odds == 2:
    for i in range(3):
        if A[i] & 1:
            A[i] += 1
    print(((A[2] * 2 - A[0] - A[1]) // 2 + 1))
else:
    for i in range(3):
        if A[i] % 2 == 0:
            A[i] += 1
    print(((A[2] * 2 - A[0] - A[1]) // 2 + 1))
