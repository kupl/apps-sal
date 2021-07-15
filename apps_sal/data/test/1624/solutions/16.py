m=int(input())
num=[int(x) for x in input().split()]
num.sort()
counter=0
for i in range(m//2):
    counter+=(num[i]+num[m-i-1])**2
print(counter)

