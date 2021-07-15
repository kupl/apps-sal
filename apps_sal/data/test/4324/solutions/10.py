t = int(input(''))
c = []
for i in range(97,123,1):
    c.append(chr(i))
for _ in range(t):
    n,a,b = list(map(int,input('').split(' ')))
    s = ''
    for i in range(n):
        s = s+c[i%b]
    print(s)
