n, m = list(map(int, input().split()))
s = input()
k = []
a = ['' for i in range(m)]
b = ['' for i in range(m)]
ans = [0 for i in range(n)]
for i in range(n):
    k.append(s[i])
d = {}
for i in range(26):
    d[chr(ord('a') + i)] = 0
for i in range(m):
    a[i], b[i] = list(map(str, input().split()))

for i in range(26):
    cur = chr(ord('a') + i)
    for j in range(m):
        if a[j] == cur or b[j] == cur:
            if a[j] == cur:
                cur = b[j]
            else:
                cur = a[j]
    d[chr(ord('a') + i)] = cur
used = [True for i in range(n)]
for i in range(26):
    for j in range(n):
        if s[j] == chr(ord('a') + i) and used[j] == True:
            ans[j] = d[chr(ord('a') + i)]
            used[j] = False
print(''.join(str(i) for i in ans))
            
    

