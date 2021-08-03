# import math
# import statistics
# import itertools
# a=int(input())
# b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
A, B = map(int, input().split())
f = list(map(int, input().split()))
# g = [input().split for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen
kyori = []
for i in range(len(f) - 1):
    an = f[i + 1] - f[i]
    kyori.append(an)

an2 = A - f[-1] + f[0]
ans = max(max(kyori), an2)
print(A - ans)
