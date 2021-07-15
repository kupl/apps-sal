N = int(input())
D = list(map(int, input().split()))

ANS = 0
for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        ANS = ANS + D[i] * D[j]
print(ANS)
