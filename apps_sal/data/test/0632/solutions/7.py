# The real secret to success is enthusiasm. Walter Chrysler
# by : Blue Edge - Create some chaos

def give(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return i
        i+=1
    return n
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    print(n+give(n)+2*(k-1))

