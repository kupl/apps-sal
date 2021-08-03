N = int(input())
A = [int(i) for i in input().split()]
B = A.copy()
OK = True
count = 0
while OK:
    for c in range(N):
        if A[c] % 2 == 0:
            A[c] = A[c] // 2
            if A[-1] == (B[-1] / (2 ** (count + 1))):
                count += 1
        else:
            OK = False
            break
print(count)
