N = int(input())
C = list(map(int, input().split()))
Alice = []
Bob = []
C = sorted(C, reverse=True)
for i in range(0, N):
    if i % 2 == 0:
        Alice.append(C[i])
    else:
        Bob.append(C[i])
print(sum(Alice) - sum(Bob))
