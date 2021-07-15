n = int(input())

def f(a):
    if a==0:
        return 0
    else:
        return f(norm(a)-1) + 1

def norm(a):
    if a > 0 and a % 2 == 0:
        while a % 2 == 0:
            a //= 2
    if a > 1:
        while (a - 1) % 4 == 0:
            a = (a - 1) // 2 + 1
    return a
    
m = sorted([f(int(x)) for x in input().split()])
s = 0
w = 0
for i in range(len(m)-1):
    if m[i] == m[i+1]:
        w += 1 
    else:
        s += (w*(w+1))//2
        w = 0
        
s += (w*(w+1))//2
print(s)
