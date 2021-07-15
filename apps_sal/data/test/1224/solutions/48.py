def II(): return int(input())
n=II()
#3**37 < 10**18 < 3**38 : 1<=a<=37
#5**25 < 10**18 < 5**26 : 1<=b<=25
for a in range(1,38):
    for b in range(1,26):
        if 3**a+5**b==n:
            print(a,b)
            return
print(-1)
