import math
n = int(input())
arr = list(map(int, input().split()))
tb = {}
# arr=sorted(arr)

for i in range(n):
    # print(i)
    if arr[i] in tb:
        x = arr[i]
        while x in tb:
            y = tb.pop(x)
            if 2 * x not in tb:
                tb[2 * x] = i
                break
            x = 2 * x
    else:
        tb[arr[i]] = i
    # print(tb)

# print(tb)
s = ''
print(len(tb))
key = list(tb.keys())
ans = []
for i in key:
    ans.append([tb[i], i])

ans.sort()

for i in ans:
    s += str(i[1]) + " "

##
# key=sorted(list(tb.keys()))
# i=0
# while j>=0:
# for i in range(len(key)):
# if key[i]%arr[j]==0:
# x=key[i]//arr[j]
# val=math.log(x,2)
# if int(val)==val:
##                s=str(key[i])+' '+s
# key[i]=-1
# print(arr[j],s)
# break
# j-=1
##

# while len(tb)>0:
# if arr[j] in tb:
##        s=str(arr[j])+' '+s
# g=tb.pop(arr[j])
# else:
# x=arr[j]
# c=0
# while (x not in tb and c<100):
# print(tb,x)
# x=2*x
# c+=1
# if c<100:
##            s=str(x)+' '+s
# g=tb.pop(x)
# j-=1

print(s)
