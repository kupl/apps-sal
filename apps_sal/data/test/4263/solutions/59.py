s = list(input()) + ['X']
l = ['A', 'G', 'C', 'T']
for i in range(len(s)):
    if s[i] in l:
        s[i] = 1
    else:
        s[i] = 0
cnt = 0
li = []
for i in range(len(s)):
    if s[i] == 1:
        cnt += 1
    else:
        li.append(cnt)
        cnt = 0
print(max(li))
