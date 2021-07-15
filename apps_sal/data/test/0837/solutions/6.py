def fi(n):
    if n == 1:
        return x
    elif n == 2:
        return x + min(x, y)
    else:
        if n % 2 == 1:
            return min(fi(n-1), fi(n+1)) + x
        else:
            return fi(n//2) + min(y, x * (n//2))
        
n,x,y = map(int, input().split())
print(fi(n))
