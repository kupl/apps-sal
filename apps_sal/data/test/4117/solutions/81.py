N = int(input())
L = list(map(int, input().split()))
count = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            temp = set([L[i], L[j], L[k]])
            if len(temp) != 3:
                continue
            ma = max(temp)
            if ma < sum(temp - {ma}):
                count += 1
print(count)
