s = input()
mid = len(s)//2
q = s[:mid]
if len(s)%2 == 0:
    t = list(s[mid:])
else:
    t = list(s[mid+1:])

t.reverse()
cnt = 0

for i in range(mid):
    cnt += s[i] != t[i]

print(cnt)
