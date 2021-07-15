n = int(input())
A = list(map(int, input().split()))
A.sort()
k = 1
for i in A:
    if i >= k:
        k += 1
print(k - 1)
