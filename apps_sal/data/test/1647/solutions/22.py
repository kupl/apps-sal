n = int(input())
a = input()
b = input()

pr = {}
ans = []

for i in range(0, 26):
    pr[i] = i

def find_set(v):
    if pr[v] == v:
        return v
    pr[v] = find_set(pr[v])
    return pr[v]

def union_set(x, y):
    pr[x] = y
    ans.append((x, y))

for i in range(len(a)):
    pa = find_set(ord(a[i]) - 97)
    pb = find_set(ord(b[i]) - 97)
    if pa == pb:
        continue
    union_set(pa, pb)

print(len(ans))
for i in ans:
    print(chr(97 + i[0]), chr(97 + i[1]))
