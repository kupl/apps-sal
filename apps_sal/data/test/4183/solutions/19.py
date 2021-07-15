import fractions
n=int(input())
t=[]
for _ in range(n):
    T=int(input())
    t.append(T)
ans=t[0]
for i in range(1, len(t)):
    ans = ans * t[i] // fractions.gcd(ans, t[i])
print(ans)    
