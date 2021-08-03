A, B, K = map(int, input().split())


array = []
for i in range(1, max(A, B) + 1):
    if (A % i == 0) and (B % i == 0):
        array.append(i)


print(array[-K])
