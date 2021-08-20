S = list(input())[::-1]
T = list(input())[::-1]
for i in range(len(S) - len(T) + 1):
    ans = S[:i]
    for j in range(len(T)):
        if S[i + j] != '?' and S[i + j] != T[j]:
            break
        else:
            ans.append(T[j])
    else:
        for j in range(i + len(T), len(S)):
            ans.append(S[j])
        print(''.join(map(str, ans[::-1])).replace('?', 'a'))
        break
else:
    print('UNRESTORABLE')
