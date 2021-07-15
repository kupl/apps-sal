n =int(input())
x = sorted(map(int,input().split()))
print(x[len(x)//2]-x[len(x)//2-1])
