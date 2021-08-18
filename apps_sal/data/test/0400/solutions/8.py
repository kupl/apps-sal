
import time


(n, k) = (int(i) for i in input().split())
A = [int(i) for i in input().split()]

start = time.time()
A = sorted(A, key=lambda x: -divmod(x, 10)[1])
B = [divmod(i, 10)[1] for i in A]

i = 0

while(k > 0 and i < len(A)):
    if B[i] == 0:
        break

    if k + B[i] - 10 > 0:
        A[i] += 10 - B[i]
        k -= 10 - B[i]
    else:
        A[i] += k
        k = 0
    i += 1

if k > 0:
    for i in range(len(A)):
        if k > 100 - A[i]:
            k -= 100 - A[i]
            A[i] = 100
        else:
            A[i] += k
            k = 0
            break

ans = sum([divmod(i, 10)[0] for i in A])
print(ans)
finish = time.time()
