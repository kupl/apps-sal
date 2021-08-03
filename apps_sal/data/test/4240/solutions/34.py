S = input()
T = input()
flag = False

for i in range(len(S)):
    if flag:
        break
    if S[i] == T[0]:
        tem = i + 1
        f = 1
        if tem == len(S):
            tem = 0
        for t in range(1, len(T)):
            if T[t] == S[tem]:
                tem += 1
                if tem == len(S):
                    tem = 0
            else:
                break
            if t == len(T) - 1:
                flag = True
if flag:
    print('Yes')
else:
    print('No')
