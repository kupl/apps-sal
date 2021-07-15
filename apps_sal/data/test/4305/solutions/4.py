H, A = list(map(int, input().split()))


if H % A == 0:
    count_e = H//A 
    print(count_e)

elif H < A:
    count_u =  1
    print(count_u)
    
elif  H % A != 0:
    count_o = H // A + 1
    print(count_o)
    

