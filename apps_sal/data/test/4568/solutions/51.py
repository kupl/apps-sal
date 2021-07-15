n = int(input())
s = input()
cnt = 0
for i in range(1,n):
    l = []
    for j in s[:i]:
        if j in s[i:]:
            l.append(j)
    l = set(l)
    cnt = max(cnt,len(l))

print(cnt)
