b = input()
f = int(b)
# a=input()
c = []
# for i in range(b):
#     c.append(a[i])
#a = list(map(int,input().split()))
#b = list(map(int,input().split()))
N = 0
for i in range(len(b)):
    c.append(int(b[i]))
d = f // int(sum(c))
e = f / int(sum(c))

if d == e:
    print("Yes")
else:
    print("No")
