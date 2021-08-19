R = {'q': 'w', 'w': 'e', 'e': 'r', 'r': 't', 't': 'y', 'y': 'u', 'u': 'i', 'i': 'o', 'o': 'p', 'a': 's', 's': 'd', 'd': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'j': 'k', 'k': 'l', 'l': ';', 'z': 'x', 'x': 'c', 'c': 'v', 'v': 'b', 'b': 'n', 'n': 'm', 'm': ',', ',': '.', '.': '/'}
L = dict()
for i in R:
    L[R[i]] = i
ch = input()
s = input()
if ch == 'R':
    dic = L
else:
    dic = R
ans = ''
for i in s:
    print(dic[i], end='')
print(ans)
