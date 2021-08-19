# I/p
# 6
# baabbb
# o/p
# bab
#
# n=int(input())
# data=input()
# val=0
# i=1
# s=""
# while val!=n:
#     s+=data[val]
#     val+=i
#     i+=1
# print(s)

# I/p
# 4
# 1 3 3 7
# O/p
# 2
# n=int(input())
# data=list(map(int,input().split()))
# data1=max(data)
# data.remove(max(data))
# a= max(data)-min(data)
# data.append(data1)
# data2=min(data)
# data.remove(min(data))
# b=max(data)-min(data)
# if a>b:
#     print(b)
# else: print(a)


# Find Divisible
# n=int(input())
# while n>0:
#     a,b=map(int,input().split())
#     while a<=b:
#         if b%a==0:
#             print(a,b)
#             break
#         b-=1
#     n-=1
# for _ in [0]*int(input()):l=int(input().split()[0]);print(l,2*l)


n = int(input())
s = input()
a = list(map(int, input().split()))

hard = {'h': 1, 'a': 2, 'r': 3, 'd': 4}

cost = [10**20, 0, 0, 0, 0]

for ai, c in zip(a, s):
    if c in hard:
        cost[hard[c]] = min(cost[hard[c] - 1], cost[hard[c]] + ai)

print(cost[4])
