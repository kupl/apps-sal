n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
flag = False
for i in range(100):
    if (i < min(b)) and (i >= max(a)) and (i >= min(a) * 2):
        if not(flag): 
            print(i)
            flag = True
if not(flag):
     print(-1)
