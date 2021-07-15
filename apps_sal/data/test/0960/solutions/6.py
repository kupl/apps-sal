n, k = map(int, input().split())
mod = k-1
while n//mod != n/mod:
    mod-=1
t = n//mod
print(t*k+mod)
