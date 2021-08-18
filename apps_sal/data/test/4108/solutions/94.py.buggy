S = input()
T = input()

trans_dict = {}

for i in range(len(S)):
    s = S[i]
    t = T[i]

    if s in trans_dict:
        if not trans_dict[s] == t:
            print('No')
            return
    else:
        trans_dict[s] = t

if len(list(trans_dict.values())) == len(set(trans_dict.values())):
    print('Yes')
else:
    print('No')
