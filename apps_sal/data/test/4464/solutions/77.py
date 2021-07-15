a,b,c = map(int,input().split())
ans = False
for i in range(b):
    if a*i%b == c :
        ans = True

print("YES" if ans else "NO")
