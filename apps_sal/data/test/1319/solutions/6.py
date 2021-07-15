n = int(input())
l = list(map(int, input().split()))
M = int(1e9+7)
counter = {}
num = 1
for elem in l:
    num = (num * elem) % M
    try:
        counter[elem]+=1
    except:
        counter[elem] = 2
        
d = 1
for elem in counter:
    d *= counter[elem]
    
res = pow(num, d//2, M)
checkodd = 1
for elem in counter:
    if counter[elem] % 2 == 0: 
        checkodd = 0
        break
if checkodd:
    for elem in counter:
        for i in range(counter[elem] // 2):
            res = (res * elem) % M
            
print(res)
