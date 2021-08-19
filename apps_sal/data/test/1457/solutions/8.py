# import string
# import sys
# import json
# import queue
# import math
# import matplotlib.pyplot as plt
# import matplotlib.patches as patch
#
# class Sheree:
#     def __init__(self,x,y,r):
#         self.x = x
#         self.y = y
#         self.r = r
#         self.to_right = 200-x+r
#         self.to_left = x-r
#
#     def have_route(self, shere):
#         return math.sqrt((self.x - shere.x)**2+(self.y-shere.y)**2) <= self.r+shere.r
#
#     def __str__(self):
#         return str(self.x)+'_'+str(self.y)+'_'+str(self.r)
#
# def bfs(start):
#     q = queue.Queue()
#     q.put(start)
#     used = {}
#     p = {}
#     d = {}
#     for i in routes:
#         used[i]=False
#         p[i]=-1
#         d[i]=0
#     p[start]=-1
#     used[start]=True
#     while(not q.empty()):
#         v = q.get()
#         for to in routes[v]:
#             if(not used[to]):
#                 used[to]=True
#                 q.put(to)
#                 d[to]=d[v]+1
#                 p[to]=v
#     return [used, d, p]
#
#
#
# n = int(input())
#
# sheres = {}
# routes = {}
# fig = plt.figure()
# plt.ylim([-100,400])
# plt.xlim([-100,400])
# plt.autoscale(True,False,False)
# for i in range(n):
#     a = input().split(' ')
#     [x,y,r] = [int(x) for x in a]
#     circle = plt.Circle((x,y),radius=r,fill=False)
#     plt.text(x,y, i)
#     fig.gca().add_artist(circle)
#     shere = Sheree(x,y,r)
#     sheres[str(shere)]=shere
# fig.gca().add_patch(patch.Rectangle((0,0),200,300,fill=False))
# fig.gca().set_aspect(1)
#
# print(sheres)
# ar = []
# for i in sheres:
#     ar.append(sheres[i])
#     for j in sheres:
#         if(i != j):
#             if sheres[i].have_route(sheres[j]):
#                 if i in routes:
#                     routes[i].add(j)
#                 else:
#                     routes[i] = set([j])
#                 if j in routes:
#                     routes[j].add(i)
#                 else:
#                     routes[j] = set([i])
#             else:
#                 if i not in routes:
#                     routes[i]=set([])
#
# ar.sort(key= lambda x: x.x)
#
# print(routes)
# res = bfs(str(ar[0]))
# print(res[0])
# print(res[1])
# print(res[2])
# fig.savefig('res.png')
# plt.show()
#


str = input()
str2 = input()

print(str.count(str2))
