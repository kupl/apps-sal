N = int(input())
A = list(map(int, input().split()))

Alice = 0
Bob = 0
for i in range(N):
    maxA = max(A)
    A.remove(maxA)
    if i % 2 == 0:
        Alice += maxA
    else:
        Bob += maxA

print("{}".format(Alice - Bob))
