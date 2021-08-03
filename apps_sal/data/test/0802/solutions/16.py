n = int(input())
s = input()
k = k1 = n
q = set()
c = 0
w = 0
t = False
for i in range(n):
    if s[i] not in q:
        q.add(s[i])
        w = i
        k1 = k = w - c + 1
while True:
    if s[c] in s[c + 1:w + 1]:
        if w - c < k1:
            k1 = w - c
            if k1 < k:
                k = k1
        c += 1
    else:
        for i in range(c + 1, n):
            if s[i] == s[c]:
                w = i
                t = True
                break
        if t == False:
            print(k)
            break
        t = False
