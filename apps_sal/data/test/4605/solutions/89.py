N,A,B = map(int,input().split())

def aaa(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n//10 
    return sum

sum = 0

for i in range(1,N+1):
    a = aaa(i)
    if A<= a <= B:
        sum += i
print(sum)
