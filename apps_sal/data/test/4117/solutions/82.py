N = int(input())
L = list(map(int, input().split()))
counter = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if len(set([L[i], L[j], L[k]])) == 3 and L[i] + L[j] > L[k] and (L[j] + L[k] > L[i]) and (L[i] + L[k] > L[j]):
                counter += 1
print(counter)
