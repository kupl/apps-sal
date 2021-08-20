from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cnt_A = Counter(A)
A_ = sorted([[k, v] for (k, v) in cnt_A.items() if v >= 2], reverse=True)
if len(A_) == 0:
    print(0)
elif A_[0][1] >= 4:
    print(A_[0][0] ** 2)
else:
    print(A_[0][0] * A_[1][0])
