n,m,r = list(map(int,input().split()))
s = min(list(map(int,input().split())))
b = max(list(map(int,input().split())))
print(max(r, r % s + (r // s) * b))

