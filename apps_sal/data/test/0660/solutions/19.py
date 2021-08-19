import queue
import math
import io


# n = int(input())
#
# class Sphere:
#     def __init__(self,x,y,r):
#         self.x = x
#         self.y = y
#         self.r = r
#         self.left =x-r
#         self.right = 300 - x+r
#
#     def has_route(self, shere):
#         return math.sqrt((self.x - shere.x)**2+(self.y-shere.y)**2) <=self.r+shere.r
#
#     def __str__(self):
#         return str(self.x)+'_'+str(self.y)+'_'+str(self.r)
#
# to_ = []
# sher = []
# sheres = {}
# sheres1 ={}
# def bfs(start):
#     q = queue.Queue()
#     q.put(start)
#     used ={}
#     d ={}
#     p ={}
#     for sher1 in sheres:
#         used[sher1]=False
#         d[sher1]=0
#         p[sher1]=0
#     used[start]=True
#     while not q.empty():
#         v = q.get()
#         for sh in sheres[v]:
#             if not used[sh]:
#                 used[sh]=True
#                 q.put(sh)
#                 d[sh]=d[v]+1
#                 p[sh]=v
#     return [used,d,p]
#
#
# for i in range(n):
#     [x,y,r] = [int(x) for x in input().split(' ')]
#     sher.append(Shere(x,y,r))
#     to_.append(sher[-1])
#     sheres1[str(sher[-1])]=sher[-1]
#
# to_.sort(key=lambda x: x.left)
#
#
#
#
# for i in range(len(sher)):
#     for j in range(len(sher)):
#         if i != j:
#             if sher[i].has_route(sher[j]):
#                 if str(sher[i]) in  sheres:
#                     sheres[str(sher[i])].append(str(sher[j]))
#                 else:
#                     sheres[str(sher[i])] = [str(sher[j])]
#             else:
#                 if str(sher[i]) not in sheres:
#                     sheres[str(sher[i])] = []
#
# [used,d,p] = bfs(str(sher[0]))
#
# print(d)
# print(p)
# print(sheres)
# print(to_)


#
# def relax(to, p):
#     v = to
#     res = []
#     while (v != -1):
#         res.append(v)
#         v = p[v]
#     return res
#
#
# [b, e, p, n, m] = [int(x) for x in input().split()]
# g = []
# for i in range(n+1):
#     g.append([])
# print(g)
# for i in range(m):
#     [to, v] = [int(x) for x in input().split()]
#     g[to].append(v)
#     g[v].append(to)
#
# [used1, d1, p1] = bfs(1, g)
# [used2, d2, p2] = bfs(2, g)
# [used3, d3, p3] = bfs(n, g)
# mi = 10 ** 10
# print(p1)
# path = relax(2,p1)
# for i in range(len(path)):
#     cur_po = path[i]
#     len_c = d3[path[i]]
#     mi = min(i*b+(len(path)-i)*e+d3[path[i]]*p, mi)
#
#
# print(min(mi, d3[1]*b+d3[2]*e))
#io1 = open('discuss.in')
s = [2, 4, 8, 16, 32, 64, 128, 256, 512]


def step(n):
    st = 0
    for i in range(len(s)):
        if(s[i] > n):
            st = s[i - 1]
            break
    return [(n - st) + st // 2, st // 2]


[n, b, p] = [int(x) for x in input().split(' ')]
res = 0
res_p = n * p
while n > 1:
    [n, rb] = step(n)
    res += rb * 2 * b + rb
print(str(res) + " " + str(res_p))
