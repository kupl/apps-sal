N = int(input())
L_l = sorted(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if L_l[i] < L_l[j] and L_l[j] < L_l[k] and (L_l[i] + L_l[j] > L_l[k]):
                ans += 1
            else:
                continue
print(ans)
