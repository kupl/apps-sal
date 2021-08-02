N = int(input())
A = list(map(int, input().split()))
X = [0, 0, 0]

for i in range(len(A)):
    if A[i] % 4 == 0:
        X[2] += 1
    elif A[i] % 2 == 0:
        X[1] += 1
    else:
        X[0] += 1

if 2 * X[2] + 1 >= N:
    print("Yes")
elif 2 * X[2] + X[1] >= N:
    print("Yes")
else:
    print("No")
