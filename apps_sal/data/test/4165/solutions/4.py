n = int(input())
l = list(map(int,input().split()))

all_l = sum(l)
max_l = max(l)

com = all_l - max_l

if(com > max_l):
    print('Yes')
else:
    print('No')

