def solve():
    s = input()
    
    a = ""
    
    for x in s:
        if x != 'a':
            a += x
    
    if len(a) == 0:
        print (s)
        return
        
    n = len(a)//2
    
    if 'a' in s[len(s)-n:]:
        print (":(")
        return
    
    print (s[:len(s)-n] if a[:n] == a[n:] else ":(")    
    
def __starting_point():  
    solve()
__starting_point()
