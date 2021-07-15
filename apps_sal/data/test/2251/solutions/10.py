# 505B.py
# Mr. Kitayuta's Colorful Graph

#First try
# n,m = map(int, raw_input().split())
# g = [[[] for _ in range(n+1)] for _ in range(m+1)]
# for i in xrange(m):
#     a,b,c = map(int, raw_input().split())
#     g[c][a].append(b)

# q = int(raw_input())

# for i in xrange(q):
#     u,v = map(int, raw_input().split())
#     out = 0
#     for j in xrange(1, len(g)):
#         u_found = v_found = False
#         for k in xrange(1, n+1):
#             if g[j][k]:
#                if k == u:
#                      u_found = True
#                elif k == v:
#                      v_found = True

#                for l in g[j][k]:
#                     if l == u:
#                         u_found = True
#                     elif l == v:
#                         v_found = True
#             if v_found == True and u_found == True:
#                 break
#         if v_found == True and u_found == True:
#             out += 1

#     print out
        
#Editorial
#DFS

#file = open("505Btest")
f = lambda: input()
#f = lambda: file.readline()
ml = lambda: list(map(int, f().split()))

n,m = ml()
g = [[ []for x in range(n+1)] for x in range(m+1)]

for i in range(m):
    a,b,c = ml()
    g[c][a].append(b)
    g[c][b].append(a)

q = int(f())

def dfs(c, start, end):
    nonlocal g, n
    discovered = [False] *(n+1)
    s = []
    s.append(start)
    while s:
        v = s.pop()
        if not discovered[v]:
            discovered[v] = True
            for i in g[c][v]:
                if i == end:
                    return True
                s.append(i)

    return False

for i in range(q):
    u,v = ml()
    count = 0
    for j in range(1, m+1):
        if g[j]:
            if dfs(j, u, v):
                count += 1
    print(count)
            

