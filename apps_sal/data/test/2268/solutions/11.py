(n, m) = list(map(int, input().split()))
alpha_cnst = list('abcdefghijklmnopqrstuvwxyz')
alpha = list('abcdefghijklmnopqrstuvwxyz')
s = input()
for i in range(m):
    (a, b) = input().split()
    for j in range(len(alpha)):
        if alpha[j] == a:
            alpha[j] = b
        elif alpha[j] == b:
            alpha[j] = a
total = ''
for char in s:
    total += alpha[alpha_cnst.index(char)]
print(total)
