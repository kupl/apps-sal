h , w = list(map(int, input().split()))
n = int(input())
a = list(map(int,input().split()))
p = []
p2 = []
j = 1
for i in a:
    p+=[str(j)]*i
    j+=1
for i in range(h):
    p2.append(p[i*w:i*w+w])
for i in range(h):
    if i%2==1:
        p2[i].reverse()
for i in p2:
    print((" ".join(i)))

