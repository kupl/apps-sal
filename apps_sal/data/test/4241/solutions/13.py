S = input()
T = input()


ans = [0] * (len(S) - len(T) + 1)

for i in range(len(S) - len(T) + 1):
    st = S[i:i + len(T)]
    for j in range(len(T)):
        if st[j] != T[j]:
            ans[i] += 1

print(min(ans))
