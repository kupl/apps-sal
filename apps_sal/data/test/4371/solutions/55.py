S = input()
ans = []
for i in range(len(S) - 2):
    temp = int(S[i:i + 3])
    ans.append(abs(753 - temp))
print((min(ans)))
