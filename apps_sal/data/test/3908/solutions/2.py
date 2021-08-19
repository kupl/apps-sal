alphabet = 'abcdefghijklmnopqrstuvwxyz'
n = input()
r = [0 for i in range(26)]
s = [[0 for i in range(26)] for j in range(26)]
if len(n) == 1:
    print(1)
else:
    for i in range(len(n)):
        t = alphabet.index(n[i])
        for j in range(26):
            s[t][j] += r[j]
        r[t] += 1
    l = [max(s[i]) for i in range(26)]
    print(max(max(r), max(l)))
