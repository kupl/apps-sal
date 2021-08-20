N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if len(set([L[i], L[j], L[k]])) == 3 and L[i] + L[j] > L[k]:
                ans += 1
print(ans)
