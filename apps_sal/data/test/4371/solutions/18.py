S = input()

S_list = []
for i in range(len(S) - 2):
    dif = abs(int(S[i] + S[i + 1] + S[i + 2]) - 753)
    S_list.append(dif)

ans = min(S_list)

print(ans)
