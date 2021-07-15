# cook your dish here
from sys import stdin,stdout
def main():
    cases = stdin.readline()
    n = int(cases)
    if n==0:
        print(n)
        return
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    count = 0
    for i in prime:
        if i==True:
            count+=1
    print(count)
def __starting_point():
    main()

__starting_point()
