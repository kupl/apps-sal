def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def max_p(n):
    if not is_prime(n):
        i = n - 2
        while (i > 0):
            if is_prime(i):
                return i
            i -= 1
    else:
        return n
            
n = int(input())

if n == 2:
    ans = 1
    
elif n % 2 == 0:
    ans = 2
else:
    ans = 1
    while not is_prime(n):
        #print(max_p(n))
        if n % 2:
            n = n - max_p(n)
            #print(n)
            ans += 1
        else:
            ans += 1
            break

print(ans)
