N = int(input())

ans = 0
d = {}

for i in range(N):
    txt = "".join(sorted(input()))
    d.setdefault(txt,0)
    
    ans += d[txt]
    d[txt] += 1
    
print(ans)
