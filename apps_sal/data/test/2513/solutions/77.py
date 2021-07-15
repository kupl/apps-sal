n = int(input())
S = input()

P = [
    ['S', 'S'],['S', 'W'],
    ['W', 'S'],['W', 'W']
]

if S[0] == 'o':
    n1 = ['S','W','W','S']
else:
    n1 = ['W','S','S','W']

for idx, p in enumerate(P):
    for i in range(1, n-1):
        if S[i] == 'o':
            if p[i] == 'S':
                p.append(p[i-1])
            else:
                p.append('W' if p[i-1] == 'S' else 'S')
        else:
            if p[i] == 'S':
                p.append('W' if p[i-1] == 'S' else 'S')
            else:
                p.append(p[i-1])
    if n1[idx] == p[-1]:
        if  (S[-1] == 'o' and n1[idx] == 'S' and p[0] == p[-2]) or\
            (S[-1] == 'o' and n1[idx] == 'W' and p[0] != p[-2]) or\
            (S[-1] == 'x' and n1[idx] == 'W' and p[0] == p[-2]) or\
            (S[-1] == 'x' and n1[idx] == 'S' and p[0] != p[-2]):
                print((''.join(p)))
                break
else:
    print((-1))

