A = [int(input()) for i in range(5)]
k = int(input())

for j in range(4):
    for h in range(j + 1, 5):
        if k < abs(A[j] - A[h]):
            print(":(")
            return
print("Yay!")
