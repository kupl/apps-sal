(N, K) = map(int, input().split())
S = input()
change = [0]
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        change.append(i + 1)
change.append(N)
r = len(change)
X = []
for i in range(r - 1):
    if S[change[i]] == '0':
        a = min(i + 2 * K, r - 1)
        X.append(change[a] - change[i])
    else:
        a = min(i + 2 * K + 1, r - 1)
        X.append(change[a] - change[i])
print(max(X))
