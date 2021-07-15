def func(n) :
    i = 1
    b = n
    while i*i <= n :
        if n % i == 0 :
            if max(len(str(i)), len(str(n//i))) < b :
                b = max(len(str(i)), len(str(n//i)))
        
        
        i += 1
    
    return print(b)        

n = int(input())
func(n)
