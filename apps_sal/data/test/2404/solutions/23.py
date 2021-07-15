a=int(input())

for i in range(2,a):
    if a%i==0:
        print(i,end="")
        print(a//i)
        break

