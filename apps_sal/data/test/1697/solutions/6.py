#f = lambda: input()
#file = open("btest", "r")
#f = lambda:file.readline()

# n, m = map(int, f().split())

# g = []

# for i in range(n):
#     g.append(f())

# disco = [[False for _ in range(m)] for _ in range(n)]

# #print(disco)
# #print(parent)
          
# def found_cycle(w):
#     nonlocal disco
#     s = []
#     s.append(w)
#     while s:
#         v = s.pop()
#         if disco[v[0]][v[1]] == False:
#             if v[0] > 0 and g[v[0]-1][v[1]] == g[v[0]][v[1]]:
#                 s.append([v[0]-1, v[1]])
                
#             if v[0] < n-1 and g[v[0]+1][v[1]] == g[v[0]][v[1]]:
#                 s.append([v[0]+1, v[1]])
                
#             if v[1] > 0 and g[v[0]][v[1]-1] == g[v[0]][v[1]]:
#                 s.append([v[0], v[1]-1])
                
#             if v[1] < m-1 and g[v[0]][v[1]+1] == g[v[0]][v[1]]:
#                 s.append([v[0], v[1]+1])
                
#         else:
#             disco[v[0]][v[1]] = True
#     return False

# found = False
# for i in range(n):
#     if found:
#         break
#     for j in range(m):
#         if disco[i][j] == False:
#             found = found_cycle([i,j])
#             break

# if found:
#     print ("Yes")
# else:
#     print ("No")

#Editorial
import sys
sys.setrecursionlimit(10000)

#file = open("btest", "r")
#f = lambda:file.readline()
f = lambda:input()

n,m = list(map(int, f().split()))

matrix = []

disco = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    matrix.append(f())

def valid_node(i, j):
    return 0 <= i < n and 0 <= j < m

def dfs(i, j, p, k, cc = 0):
    if disco[i][j] == k:
        return True
    
    disco[i][j] = k

    res = False
    dd = [[0,1], [1,0], [-1,0], [0,-1]]
    for d in dd:
        if valid_node(i+ d[0], j+d[1]) and (i + d[0] != p[0] or j + d[1] != p[1]):
            if matrix[i + d[0]][j+ d[1]] == matrix[i][j]:
                res = res or dfs(i + d[0], j+d[1], [i,j], k, cc+1)

    return res

ok = False
k = 1
for i in range(n):
    for j in range(m):
        if disco[i][j] == 0:
            ok = ok or dfs(i, j, [i, j], k)
            k += 1

if ok:
    print("Yes")
else:
    print("No")

