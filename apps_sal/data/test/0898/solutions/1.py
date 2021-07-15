def prime(n):
    l = [[], []]
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i*i == n:
                l[0].append(i)
            else:
                l[0].append(i)
                l[1].append(n//i)
    return l[0]+l[1][::-1]
n, m = map(int, input().split())
x = 0
for i in prime(m):
    if i <= m//n:
        x = i
print(x)
