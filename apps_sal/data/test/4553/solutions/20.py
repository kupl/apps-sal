a,b = list(map(int,input().split()))
s = input()

num = list(map(str,list(range(10))))

flag = True
for i in range(a):
    if s[i] not in num:
        flag = False
if s[a] != "-":
    flag = False
for i in range(a+1,a+b+1):
    if s[i] not in num:
        flag = False

if flag:
    print("Yes")
else:
    print("No")

