
def mi():
    return map(int, input().split())


n = int(input())
s = list(input())
t = list(input())
inp1 = s.copy()
inp2 = t.copy()
if sorted(s) != sorted(t):
    print(-1)
else:
    out1 = []
    c1 = 0
    c2 = 0
    out2 = []
    for i in range(n):
        if s[i] == t[i]:
            continue
        for j in range(i + 1, n):
            if s[j] == t[i]:
                index = j
                break
        s[i + 1:index + 1] = s[i:index]
        s[i] = t[i]
        for j in range(index, i, -1):
            c1 += 1
            out1.append(j)
    print(c1)
    for i in out1:
        print(i, end=' ')
