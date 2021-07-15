n,a,b = map(int, input().split())
c = a+b
quo = n//c
mod = n%c
ans = a*quo + min(mod,a)
print(ans)
