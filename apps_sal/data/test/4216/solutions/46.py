def digit(a,b):
    a = str(a)
    b = str(b)
    return max(len(a),len(b))

def makedivisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n//i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
l = makedivisors(n)
m = 10**9
for a in range(len(l)):
    for b in range(len(l)):
        if l[a] * l[b] == n:
            m = min(m,digit(l[a],l[b]))
print(m)
    

