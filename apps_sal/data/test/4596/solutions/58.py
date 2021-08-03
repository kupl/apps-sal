N = int(input())
A = list(map(int, input().split()))
count = 0
roop = True

while roop == True:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] /= 2
        else:
            roop = False
            break
    if roop == True:
        count += 1
print(count)
