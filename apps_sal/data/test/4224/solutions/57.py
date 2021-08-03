N = int(input())
A = list(map(int, input().split()))
counter = []
for num in range(len(A)):
    counter.append(0)
for num in range(len(A)):
    while A[num] % 2 == 0:
        A[num] = A[num] / 2
        counter[num] += 1
print((sum(counter)))
