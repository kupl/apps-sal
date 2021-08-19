(N, X) = list(map(int, input().split()))
L = list(map(int, input().split()))
S = [0]
sum_L = 0
for i in range(N):
    sum_L += L[i]
    S.append(sum_L)
counter = 0
for i in range(N + 1):
    if S[i] <= X:
        counter += 1
print(counter)
