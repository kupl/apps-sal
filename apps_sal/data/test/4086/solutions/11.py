n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a[::-1]:
    if i not in b:
        b.append(i)
print(len(b))
print(*b[::-1])

