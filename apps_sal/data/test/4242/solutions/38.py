(A, B, K) = map(int, input().split())
arr = []
for i in range(1, max(A, B) + 1):
    if A % i == 0 and B % i == 0:
        arr.append(i)
print(sorted(arr)[-K])
