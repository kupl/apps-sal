(n, m) = list(map(int, input().split()))
S = input()
S1 = input()
t = []
for i in range(m - n + 1):
    k = 0
    t1 = []
    V = ''
    for j in range(i, i + n):
        if S1[j] != S[j - i]:
            t1.append(j - i + 1)
    t1 = [len(t1)] + t1
    t.append(t1)
t = sorted(t)
print(t[0][0])
print(*t[0][1:])
