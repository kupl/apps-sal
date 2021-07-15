n,a,b,c = list(map(int, input().split()))
l = []
if (n%4==0):
    l = [0]
elif(n%4==1):
    l = [3*a,a+b,c]
elif(n%4==2):
    l = [2*a, b, 2*c]
else:
    l = [a, b+c, 3*c]

mini = min(l)
print(mini)

