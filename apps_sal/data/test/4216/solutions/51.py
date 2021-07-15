n = int(input())
def f(a,b):
    a = list(str(a))
    b = list(str(b))
    return max(len(a),len(b))

m = float('inf')
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        m = min(m,f(i,n//i))
print(m)

