# cook your dish here

x, y = input().split()
x=int(x)
y=float(y)

if x%5==0 and y-x>=0.5 :
    y = y - x - 0.5
print(y)
