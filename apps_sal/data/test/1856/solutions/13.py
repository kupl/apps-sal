import sys
import string

def input():
    return sys.stdin.readline().strip()

def dfs(i,vis,al):
    vis[i] = True
    for j in al[i]:
        if not vis[j]:
            dfs(j,vis,al)

al = [list() for _ in range(26)]
got = set()
n = int(input())
for _ in range(n):
    s = input()
    s = set([ord(c)-ord('a') for c in s])
    s = list(s)
    for i in range(len(s)):
        got.add(s[i])
        for j in range(i+1,len(s)):
            al[s[i]].append(s[j])
            al[s[j]].append(s[i])
vis = [False]*26

cnt = 0
for i in range(26):
    if not vis[i] and i in got:
        #print(got)
        dfs(i,vis,al)
        cnt+=1
print(cnt)




