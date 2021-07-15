def gcd(n1,n2):
    if n2 > n1:
        return gcd(n2,n1)
    if n2 == 0:
        return n1
    return gcd(n2,n1%n2)

def factors(n):
    ans = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ans += 1
            if i != n//i:
                ans += 1

    return ans

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    g = 0
    for i in arr:
        g = gcd(i,g)
    
    facts = factors(g)
    print(facts)

main()

