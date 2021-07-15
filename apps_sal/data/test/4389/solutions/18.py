t=int(input())
for i in range(t):
    a=input()
    s=a[0]+a[1:len(a)-1:2]+a[-1]
    print(s)
