b1, q, l, m = map(int, input().split())
num1 = list(map(int, input().split()))
num = set(num1) 
if q == 1 and abs(b1) <= l: 
    if b1 in num: 
        print(0) 
    else:
        print("inf")
    return 
    
if q == -1 and abs(b1) <= l:
    if b1 in num: 
        if -b1 in num:
            print(0)
        else: 
            print("inf")
        return 
    print("inf")
    return
        
if q == 0 and abs(b1) <= l:
    if b1 in num:
        if 0 in num: 
            print(0)
        else: 
            print("inf") 
        return
    if 0 in num:
        print(1)
    else: 
        print("inf")
    return

if b1 == 0 and b1 <= l:
    if 0 in num: 
        print(0)
    else:
        print("inf") 
    return 
if b1 == 1 and (q == 1) and b1 <= l: 
    if 1 in num: 
        print(0)
    else:
        print("inf")
    return
if b1 == -1 and q == 1 and b1 <= l:
    if -1 in num: 
            print(0)
    else:
        print("inf")
    return    
if b1 == 1 and q == -1  and b1 <= l: 
    if 1 in num:
        if -1 in num: 
            print(0)
        else: 
            print("inf")
    else: 
        print("inf")
    return
if b1 == -1 and q == -1 and b1 <= l:
    if -1 in num:
        if 1 in num: 
            print(0)
        else: 
            print("inf")
    else: 
        print("inf")
        return    
ans = 0
while l >= abs(b1): 
    if b1 not in num: 
        ans += 1 
    b1 *= q
print(ans)
