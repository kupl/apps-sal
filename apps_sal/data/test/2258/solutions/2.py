"""T=int(input())
for _ in range(0,T):
    n=int(input())
    a,b=map(int,input().split())
    s=input()
    s=[int(x) for x in input().split()]
    for i in range(0,len(s)):
        a,b=map(int,input().split())"""
n = int(input())
s = [int(x) for x in input().split()]
kk = []
for i in range(n):
    h = []
    kk.append(h)
for i in range(0, len(s)):
    for j in range(i + 1, len(s)):
        if s[i] > s[j]:
            kk[j].append((s[i], i))
for i in range(0, n):
    kk[i].sort()
fnl = []
for i in range(n - 1, -1, -1):
    for j in range(0, len(kk[i])):
        fnl.append((i, kk[i][j][1]))
print(len(fnl))
for i in range(0, len(fnl)):
    print(fnl[i][1] + 1, fnl[i][0] + 1)
