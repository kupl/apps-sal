N = int(input())
A = list(map(int, input().split()))
Q = int(input())

num = [0] * (10 ** 5 + 1)
for ai in A:
    num[ai] += 1

S = sum(A)
for i in range(Q):
    B, C = map(int, input().split())
    S += (C - B) * num[B]
    num[C] += num[B]
    num[B] = 0
    print(S)

return
