from collections import Counter
n = int(input())
mod = 10**9 + 7
A = list(map(int, input().split()))

C = Counter(A)
if n % 2 == 0:
    for i in range(1, n, 2):
        if C.get(i) != 2:
            print(0)
            return
else:
    if C.get(0) != 1:
        print(0)
        return
    for i in range(2, n, 2):
        if C.get(i) != 2:
            print(0)
            return

n //= 2
print(pow(2, n, mod))
