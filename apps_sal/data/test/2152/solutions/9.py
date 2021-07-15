n = int(input())

pmin = 1000

sum = 0

for i in range(n):
    a, p = map(int, input().split())
    if p < pmin:
        pmin = p
    sum += a * pmin
    
print(sum)
