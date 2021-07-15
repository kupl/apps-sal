n = int(input())
al = [int(input()) for i in range(n)]

i = 0
for j in range(n):
    i = al[i]-1
    if i == 1:
        print(j+1)
        return
print(-1)
