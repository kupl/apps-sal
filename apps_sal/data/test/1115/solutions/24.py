
n = int(input())
l = list(map(int,input().strip().split(' ')))
ans = sum(l)
t = int(input())
p = -1
flag = True
for _ in range(t):
    l,h = list(map(int,input().strip().split(' ')))
    if l<= ans and ans<=h and flag:
        p = ans
        flag = False
    if ans <l and flag :
        p = l
        flag = False
print(p)

