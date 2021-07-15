t, s, q = list(map(int, input().split(" ")))
ans = 0
while s < t:
    ans += 1
    s = s * q
    
print (ans)



