n = int(input())
s = list(map(int,input().split()))
t = s.copy()
t.sort()
cnt = 0
for i in range(n):
    if s[i] != t[i]:
        cnt += 1
if cnt<3:
    print("YES")
else:
    print("NO")
