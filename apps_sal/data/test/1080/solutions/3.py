n = int(input())
A = [int(x) for x in input().split()]
mx = max(A)
if mx <= sum(A) - mx and sum(A) % 2 == 0:
    print('YES')
else:
    print('NO')
