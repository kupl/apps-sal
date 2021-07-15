n,m=list(map(int,input().split()))
student=[]
for _ in range(n):
    a,b=list(map(int,input().split()))
    student.append([a,b])

checkpoint =[]
for _ in range(m):
    c,d = list(map(int,input().split()))
    checkpoint.append([c,d])

for i in range(n):
    s = student[i]
    dist = float('inf')

    num=0
    for j in range(m):
        c=checkpoint[j]
        tmp = abs(s[0]-c[0]) + abs(s[1]-c[1])

        if tmp < dist:
            dist = tmp
            num=j+1

    print(num)
        

