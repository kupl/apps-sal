# import math
# import statistics
# import itertools
a = int(input())
# b=input()
# c=[]
# for i in a:
#     c.append(int(i))
# N,K= map(int,input().split())
f = list(map(int, input().split()))
# g = [int(input()) for _ in range(N)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen
ans = [f[0], f[-1]]
for i in range(a - 2):
    ans.append(min(f[i], f[i + 1]))

print(sum(ans))
