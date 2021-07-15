S = str(input())
L = int(S[0])*10 + int(S[1]) 
R = int(S[2])*10 + int(S[3]) 

if 12 >= L >= 1:
    if 12 >= R >= 1:
        print('AMBIGUOUS')
        return
    print('MMYY')
    return

else:
    if 12 >= R >= 1:
        print('YYMM')
        return
    print('NA')
    return
