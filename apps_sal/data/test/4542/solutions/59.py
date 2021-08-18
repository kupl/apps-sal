S = input()
S = S + '1'

cnt = []
conti = 1
for i in range(1, len(S)):
    if S[i - 1] == S[i]:
        conti += 1
    else:
        cnt.append(conti)
        conti = 1
print(len(cnt) - 1)
