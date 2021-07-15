q = int(input())

for x in range(q):
    n = int(input())

    s = str(input())
    
    f = False
    for x in range(n // 2):
        if abs(ord(s[x]) - ord(s[n - x - 1])) > 2 or abs(ord(s[x]) - ord(s[n - x - 1])) == 1:
               f = True
               break
    if f:
        print("NO")
    else:
        print("YES")
    

