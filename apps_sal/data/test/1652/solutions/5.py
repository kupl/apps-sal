S = input()
S = S[::-1]

ws = ['maerd','remaerd','esare','resare']
i = 0
while i < len(S):
    for w in ws:
        if w == S[i:i+len(w)]:
            i += len(w)
            break
    else:
        print('NO')
        return
print('YES')
