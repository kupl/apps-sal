n = int(input())
x = ['M', 'S', 'L', 'XS', 'XXS', 'XXXS', 'XL', 'XXL', 'XXXL']
a = [0] * len(x)
b = [0] * len(x)
for i in range(n):
    a[x.index(input())] += 1
for i in range(n):
    b[x.index(input())] += 1

ans = 0
for i in range(len(a)):
    xx = min(a[i], b[i])
    a[i] -= xx
    b[i] -= xx
    
for i in a:
    ans += i
            
print(ans)
