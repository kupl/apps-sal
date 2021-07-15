n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aa = 0
bb = 0
for i in range(n):
    if a[i] != b[i] and a[i] == 1:
        aa+=1
    elif a[i] != b[i] and b[i] == 1:
        bb+=1
if aa == 0:
    print(-1)
else:
    print(bb // aa + 1)
