N = int(input())
L = list(map(int, input().split()))
count = 0
for i in range(0, N - 2):
    for j in range(1, N - 1):
        for k in range(2, N):
            if (i < j) & (j < k) & (L[i] != L[j]) & (L[j] != L[k]) & (L[k] != L[i]) & ((L[i] + L[j] > L[k]) & (L[j] + L[k] > L[i]) & (L[k] + L[i] > L[j])):
                count += 1
print(count)
