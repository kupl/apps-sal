s = int(input())

a = [0]*(10**6+1)
c = [0]*(10**6+1)
a[1] = s
c[s] = 1
for i in range(2, 10**6+1):
    v = a[i-1]//2 if a[i-1] % 2 == 0 else 3*a[i-1]+1
    a[i] = v
    if c[v] == 1:
        print(i)
        return
    c[v] = 1
