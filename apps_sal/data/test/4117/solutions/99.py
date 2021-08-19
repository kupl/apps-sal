n = int(input())  # ->n=5
L = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if not (i < j < k):
                continue
            if len(set([L[i], L[j], L[k]])) < 3:
                continue
            if (L[i] + L[j] > L[k]) and (L[j] + L[k] > L[i]) and (L[k] + L[i] > L[j]):
                count += 1

print(count)
