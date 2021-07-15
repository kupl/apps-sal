X=int(input())
n=100
year=0
while n<X:
    n+=n//100
    year+=1
print(year)
