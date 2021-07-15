for u in range(int(input())):
    x, y, z = map(int, input().split())
    
    t = max(x, y, z)
    ans = 0
    if t == x:
        ans += 1
    if t ==y:
        ans += 1
    if t == z:
        ans += 1
    
    if ans >=2:
        print("YES")
        print(min(x,y,z), min(x, y, z), t)
    else:
        print('NO')
