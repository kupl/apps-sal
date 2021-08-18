S = input()
T = input()
length = len(S)
keep_S = [[] for i in range(26)]  # ord(T[i])に対応する S を格納
keep_T = [[] for i in range(26)]  # ord(S[i])に対応する T を格納

for i in range(length):

    num_S = ord(T[i]) - ord('a')
    num_T = ord(S[i]) - ord('a')

    if S[i] in keep_S[num_S]:
        continue
    else:
        keep_S[num_S].append(S[i])

    if T[i] in keep_T[num_T]:
        continue
    else:
        keep_T[num_T].append(T[i])


for i in range(26):
    if (len(keep_T[i]) > 1) | (len(keep_S[i]) > 1):
        print('No')
        return
print('Yes')
