def f(i):
    return str(i) if i != p else "(" + str(i) + ")"

s = input()
n, p, k = map(int, s.split())

l, r = max(1, p-k), min(n, p+k)
ans = "<< " if l != 1 else ""
for i in range(l, r):
    ans += (f(i) + " ")
ans += f(r)    

if r != n:
    ans += " >>"
    
print(ans)
