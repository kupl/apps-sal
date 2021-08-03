# import math
# import statistics
a = int(input())
# b,c=int(input()),int(input())
# c=[]
# for i in a:
#    c.append(i)
# e1,e2 = map(int,input().split())
# f = list(map(int,input().split()))
#g = [input() for _ in range(a)]

da = True
ap = [a]
count = 1
while da:
    if a % 2 == 0:
        a = a // 2
        ap.append(a)
    elif a % 2 == 1:
        a = 3 * a + 1
        ap.append(a)
    count += 1
    if len(set(ap)) < len(ap):
        print(count)
        da = False
