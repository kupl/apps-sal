n = int(input())
a = list(map(int,input().split()))

b = [-1] * n
l = 0
r = n-1
for i in range(n-1, -1, -1):
    if i % 2:
        b[l] = a[i]
        l += 1
    else:
        b[r] = a[i]
        r -= 1

if n % 2:
    b.reverse()
b = [str(i) for i in b]
print(' '.join(b))
