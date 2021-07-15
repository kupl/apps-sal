from math import log
n = int(input())
a = [i for i in range(n + 1)]

def ans(n):
    if n <= 0 or n % 2:
        return
    j, cr = (1 << int(log(n, 2))), 1
    while j + cr - 1 <= n:
        a[j - cr], a[j + cr - 1] = a[j + cr - 1], a[j - cr]
        cr += 1
    ans(j - cr)
    
if n % 2 == 0:
    ans(n)
    print("YES")
    print(*a[1:])
else:
    print("NO")

if n <= 5 or (1 << int(log(n, 2))) == n:
    print("NO")
    return
    
print("YES")
print("3 6 1 5 4 2" if n <= 6 else "3 6 1 5 4 7 2", end=' ')
cr = 8
v = (1 << int(log(n, 2)))
for i in range(8, n + 1):
    if i >= v:
        print(n if i == v else i - 1, end=' ')
        continue
    if i == cr:
        cr *= 2
        print(cr - 1, end=' ')
    else:
        print(i - 1, end=' ')

    

