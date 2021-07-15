n = int(input())
l = [0]*n
for i in range(n):
    l[i] = list(map(int,input().split()))

l.sort(key = lambda x:x[1])

cnt = 0
for i in range(n):
    cnt += l[i][0]
    if cnt > l[i][1]:
        print("No")
        return

print("Yes")
