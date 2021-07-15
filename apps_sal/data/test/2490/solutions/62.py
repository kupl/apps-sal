#E
#greedy 
n = input()
n = n[::-1] + "0"
l = len(n)

ans = 0

kuriagari=0

for i,v in enumerate(n):
    v = int(v)
    if kuriagari:
        v += 1
    
    if v<5:
        ans += v
        kuriagari = 0
    if v>5:
        ans += 10 - v
        kuriagari = 1
    if v==5:
        if int(n[i+1])<5:
            #delete is better
            ans += v
            kuriagari = 0
        if int(n[i+1])>=5:
            #kuriagari is promising
            ans += 10 - v
            kuriagari = 1
        
print(ans)
