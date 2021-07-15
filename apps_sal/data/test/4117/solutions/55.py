N = int(input())
L = list(map(int,input().split()))
count = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if not (i < j < k):
                continue
            if len(set([L[i],L[j],L[k]])) < 3:
                continue
            if L[i] + L[j] > L[k] and L[i] + L[k] > L[j] and L[j] + L[k] > L[i]:
                count += 1
print(count)
