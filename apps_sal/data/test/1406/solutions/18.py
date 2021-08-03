a = input()
b = a.split()
n = int(b[0])
k = int(b[1])
d = int(b[2])
raw = [' '] * n
if n > k**d:
    print(-1)
    return
table = [[1] * d]
p = 1
for i in range(d):
    cv = 1
    for j in range(n):
        if j % p == 0 and j != 0:
            cv = cv + 1
            if cv == k + 1:
                cv = 1
        raw[j] = str(cv)
    print(' '.join(raw))
    p = p * k
