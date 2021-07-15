
S = input()
S = S[::-1]

l = ['maerd','remaerd','esare','resare']
i = 0
while i < len(S):
    for w in l:
        if w == S[i:i+len(w)]:
            i += len(w)
            break
    else:
        print('NO')
        return
print('YES')
