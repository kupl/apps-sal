S = list(input())
T = list(input())
S.reverse()
T.reverse()
flag = False
for i in range(len(S)-len(T)+1):
    k = 0
    for t in range(i,i+len(T)):
        if S[t] != '?' and S[t] != T[k]:
            break
        k += 1
        if k == len(T):
            flag = True
            w = i
    if flag:
        break
t = 0
if flag:
 for i in range(w,w+len(T)):
    S[i] = T[t]
    t += 1
 S.reverse()
 an = ''
 for i in range(len(S)):
    if S[i] == '?':
        an += 'a'
    else:
        an += S[i]
 print(an)
else:
    print('UNRESTORABLE')
