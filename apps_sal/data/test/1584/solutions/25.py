N = int(input())
L = list(map(int, input().split()))
ans = 0
c = [0] * 1001
for i in L: c[i] += 1
for i in range(1000): c[i + 1] = c[i] + c[i + 1]
for i in range(N - 1):
    for j in range(i + 1, N):
        l, r = abs(L[i] - L[j]), min(L[i] + L[j] - 1, 1000)
        ans += c[r] - c[l]
        if l < L[i] and L[i] <= r: ans -= 1
        if l < L[j] and L[j] <= r: ans -= 1
print(ans // 3)
