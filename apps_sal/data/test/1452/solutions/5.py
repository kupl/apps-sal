H, W = list(map(int, input().split()))
R = [int(a) for a in input().split()]
C = [int(a) for a in input().split()]

ans = 0
for i in range(H):
    for j in range(W):
        if (R[i] == j and C[j] > i) or (R[i] > j and C[j] == i):
            print(0)
            return
        if R[i] < j and C[j] < i:
            ans += 1
print(pow(2, ans, 10**9 + 7))
