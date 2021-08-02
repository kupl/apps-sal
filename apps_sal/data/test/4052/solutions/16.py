n = int(input())
s = input()
t = input()
s = list(s)
t = list(t)
A = [0] * 26
B = [0] * 26
for i in range(n):
    x = ord(t[i]) - ord('a')
    y = ord(s[i]) - ord('a')
    A[x] += 1
    B[y] += 1
if A == B:
    M = []
    for i in range(n):
        if s[i] == t[i]:
            continue
        for j in range(i, n):
            f = j
            if s[j] == t[i]:
                break
        for k in range(f, i, -1):
            M.append(k)
            s[k], s[k - 1] = s[k - 1], s[k]
    print(len(M))
    print(*M)
else:
    print(-1)
