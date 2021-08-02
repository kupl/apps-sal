tak = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}

tok = 'AHIMOoTUVvWwXxY'

s = input()
le = len(s)
le2 = le // 2

if (1 == le & 1) and not s[le2] in tok:
    print("NIE")
    return

s1 = s[0:le2]
s2 = s[le2 + (le & 1):][::-1]


for i in range(0, le2):

    if s1[i] == s2[i] and s1[i] in tok: continue
    if s1[i] in tak and tak[s1[i]] == s2[i]: continue
    print("NIE")
    return

print("TAK")
