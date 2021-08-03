N = int(input())
A = list(map(int, input().split()))

cnt = 0

for a in A:
    if a < 0:
        cnt += 1

A = list(map(lambda x: abs(x), A))
sum_A = sum(A)

if cnt % 2 == 0:
    print(sum_A)

else:
    A.sort()
    print(sum_A - 2 * min(A))
