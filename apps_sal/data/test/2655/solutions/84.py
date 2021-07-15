n = int(input())
a = list(map(int, input().split()))

a.sort()

if n % 2 == 0:
    suma = 2*sum(a[-int((n/2)):])-a[-1]
else:
    suma = 2*sum(a[-int(((n+1)/2)):])-a[-1]-a[-int(((n+1)/2))]

print(suma)
