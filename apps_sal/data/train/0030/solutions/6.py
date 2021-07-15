import sys

def main():
    n = int(sys.stdin.readline().strip())
    #n, m = map(int, sys.stdin.readline().split())
    #q = list(map(int, sys.stdin.readline().split()))
    s = sys.stdin.readline().strip()
    res = 0
    i = 0
    while i < n:
        while i < n and s[i] != "1":
            i += 1
        if i >= n:
            break
        while i < n and s[i] == "1":
            i += 1
            res += 1
            #print(i, res)
        i += 1
        res -= 1
        #print(" ", i, res)
    i = 0
    ans = 0
    while i < n:
        while i < n and s[i] != "0":
            i += 1
        if i >= n:
            break
        while i < n and s[i] == "0":
            i += 1
            ans += 1
            #print(i, res)
        i += 1
        ans -= 1
        #print(" ", i, res)
    print(max(ans, res))
    
   
        
        
            
        
                
            
            
        
            
    
    
    
    
    
    
            
                
        
    
            
        

            
        
    
                
    
    
    
            
    
        
    

for i in range(int(sys.stdin.readline().strip())):
    main()
