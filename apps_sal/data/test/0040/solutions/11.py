t = int(input())
f = 1
g = 0
a = []
while(t):
    t -= 1
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    if(a[i][0] != a[i][1]):
        f = 0
    if(i != 0 and a[i][0] > a[i - 1][0]):
        g = 1
if(f == 0):
    print("rated")
else:
    if(g):
        print("unrated")
    else:
        print("maybe")
