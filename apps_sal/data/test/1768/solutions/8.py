import sys
input = sys.stdin.readline

n = int(input())
s = input()[:-1]
ans = [[-1]*(n+1) for _ in range(26)]

for c in range(26):
    for i in range(n):
        cnt = 0
        
        for j in range(i, n):
            if ord(s[j])-ord('a')!=c:
                cnt += 1
                
            ans[c][cnt] = max(ans[c][cnt], j-i+1)
            
for c in range(26):
    for i in range(1, n+1):
        ans[c][i] = max(ans[c][i], ans[c][i-1])

for _ in range(int(input())):
    m, c = input().split()
    print(ans[ord(c)-ord('a')][int(m)])
