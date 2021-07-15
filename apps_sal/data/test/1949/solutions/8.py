t = input().split(' ')
n, k = int(t[0]), int(t[1])
T = input().split(' ')
for i in range(n):
    T[i] = int(T[i])
T.sort()
d = 0
l = 0
j = 0
for i in range(k):
    while d < len(T) and T[d] <= j:
        d+=1
    if d < len(T):
        print(T[d]-j)
        j=T[d]
    else:
        print(0)

