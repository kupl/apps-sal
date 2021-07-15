#9 B - Choose Integers AC(hint)
A,B,C = map(int,input().split())

result = 'NO'

num = 0
#(k+B)A%B = (kA + AB)%B = kB
for i in range(1,B+1):
    num = (A*i)%B
    if num == C:
        result = 'YES'
        break
print(result)    
