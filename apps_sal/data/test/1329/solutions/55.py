c=[0]*101
for i in range(1,int(input())+1):
    for j in range(2,i+1):
        while i%j==0:
            c[j]+=1
            i//=j
def f(n):
    return sum(i>n-2 for i in c)
print(f(75)+f(25)*(f(3)-1)+f(15)*(f(5)-1)+f(5)*(f(5)-1)*(f(3)-2)//2)
