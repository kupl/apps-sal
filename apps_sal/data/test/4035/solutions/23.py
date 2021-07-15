a,b = list(map(int,input().split()))

ans = -1

for price in range(10000):
    tax_a = int(price * 0.08)
    tax_b = int(price * 0.1)
    
    if tax_a == a and tax_b == b:
        ans = price
        break
        
print(ans)
