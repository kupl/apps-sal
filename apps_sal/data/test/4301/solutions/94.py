n = int(input())
a = [int(input()) for i in range(n)]
b=sorted(a)
c,d=b[-1],b[-2]
for i in a:
    print(c if i!=c else d)
