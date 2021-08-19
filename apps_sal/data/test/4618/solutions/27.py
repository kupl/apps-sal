S = input()
k = int(input())
ss = []
for i in range(len(S)):
    for j in range(i + 1, min(i + k + 1, len(S) + 1)):
        ss.append(S[i:j])
ss = sorted(list(set(ss)))
print(ss[k - 1])
