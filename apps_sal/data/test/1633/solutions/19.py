def Main():
    string = (input()).split(" ")
    n = int(string[0]) 
    m = int(string[1])
    k = int(string[2])
    
    # exit immediately if smth wrong
    if k =="0" or n == "0" or m == "0":
        print ("0")
        return
    
    mas = []
    for i in range(n):
        mas.append([])
        for j in range(m):
            mas[i].append(0)
    
    act  = True
    l = 0
    while (act and k):
        string =(input()).split(" ") 
        i = int(string[0])-1
        j = int(string[1])-1
        
    #   i = i -1
    #   j = j -1
        
        mas[i][j] = 1
        k = k - 1
        l = l + 1
        act = check(i,j,n,m,mas) 
    
    if act == True:
        print ("0")
        return
    if act == False:
        while(k):
            string = input()
            k = k-1
        print(str(l))
        return

def check (i,j,n,m,mas):            
    if i != 0:
        if j != 0:
            if mas[i-1][j-1] == 1:
                if mas[i-1][j] == 1:
                    if mas [i][j-1] == 1:
                        return False 
    if i+1 != n:
        if j+1 != m:
            if mas[i+1][j+1] == 1:
                if mas[i][j+1] == 1:
                    if mas[i+1][j] == 1:
                        return False
    if i != 0:
        if j+1 != m:
            if mas[i-1][j+1] == 1:
                if mas[i-1][j] == 1:
                    if mas[i][j+1] == 1:
                        return False
    if i+1 != n:
        if j != 0:
            if mas[i+1][j-1] == 1:
                if mas[i][j-1] == 1:
                    if mas[i+1][j] == 1:
                        return False
    return True

def __starting_point():
    Main()

__starting_point()
