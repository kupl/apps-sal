n = int(input())
s = 0
s+=n//100
n=n%100
s+=n//20
n=n%20
s+=n//10
n=n%10
s+=n//5
n=n%5
s+=n
print(s)
