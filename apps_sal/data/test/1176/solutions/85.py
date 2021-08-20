n = int(input())
A = list(map(int, input().split()))
cnt = 0
A_ = []
for i in A:
    if i < 0:
        cnt += 1
        A_.append(-i)
    else:
        A_.append(i)
if cnt % 2 == 0:
    print(sum(A_))
else:
    print(sum(A_) - 2 * min(A_))
