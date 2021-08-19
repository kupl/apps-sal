def rps(x, y):
    if x == 'R' and y == 'P':
        return y
    if x == 'P' and y == 'S':
        return y
    if x == 'S' and y == 'R':
        return y
    else:
        return x


(n, k) = map(int, input().split())
s = input()
S = s + s
for i in range(k):
    tmp = []
    for j in range(0, len(S), 2):
        tmp.append(rps(S[j], S[j + 1]))
    S = tmp + tmp
print(S[0])
