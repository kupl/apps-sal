n=int(input())
d=[0]*51
for i in input().split(" "):
    d[int(i)]+=1
for i in range(50):
    if (d[i]>n/2):
        print("Bob")
        break
    else:
        if (d[i]>0):
            print("Alice")
            break
