n = int(input())
a = list(map(int,input().split()))
b = [None] *n
for idx,person in enumerate(a):
    b[person-1] = idx+1
for j in b:
    print(j,end=' ')
