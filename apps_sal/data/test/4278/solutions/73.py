import collections
N=int(input())
S = collections.Counter([''.join(sorted(input())) for i in range(N)])
print(sum(map(lambda x: x*(x-1)//2, S.values())))
