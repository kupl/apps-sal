n = int(input())

if n % 2 != 0:
    print(0)
else:
    ans = 0
    n //= 2
    while n:
        ans += n//5
        n //= 5
    
    
    print(int(ans))
