N = int(input())
L = list(map(int, input().split()))

count = 0
for i in range(0, N - 2):
    for j in range(0, N - i - 2):
        for k in range(0, N - 2 - j - i):
            if L[i] != L[j + 1 + i] and L[i] != L[k + i + 2 + j] and L[j + 1 + i] != L[k + 2 + i + j]:
                if L[i] + L[j + 1 + i] > L[k + 2 + i + j] and L[i] + L[k + 2 + i + j] > L[j + 1 + i] and L[k + 2 + i + j] + L[j + 1 + i] > L[i]:
                    count += 1

print(count)
