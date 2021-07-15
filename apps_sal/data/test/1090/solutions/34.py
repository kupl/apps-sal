n,k = map(int,input().split())
s = [" "]+list(input())+[" "]
tar = now = s[1]
cnt = 0
for i in range(1,n+1):
    if now != s[i]:
        now = s[i]
        if now != tar: cnt += 1
    if cnt > k: break
    s[i] = tar
ans = 0
for i in range(1,n+1):
    if s[i] == "L" and s[i-1] == "L": ans += 1
    if s[i] == "R" and s[i+1] == "R": ans += 1
print(ans)
