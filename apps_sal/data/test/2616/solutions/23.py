n = int(input())

for i in range(n):
    q =  int(input())
    r = [int(p) for p in input().split(' ')]
    z = 0
    
    c = 0
    while (r[z] == 1) and (z < q-1):
        c = 1- c
        z +=1
    x = 'First' if c == 0 else 'Second'   
    print(x)  
