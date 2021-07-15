def main():
    n = int(input())
    inlis = list(map(int, input().split()))

    tmp = 0
    dic1 = {}
    dic2 = {}

    for i in range(n):
        if i % 2 == 0:
            if inlis[i] in dic1:
                dic1[inlis[i]] += 1
            else:
                dic1[inlis[i]] = 1
        else:
            if inlis[i] in dic2:
                dic2[inlis[i]] += 1
            else:
                dic2[inlis[i]] = 1
    diclis1 = list(dic1.items())
    diclis2 = list(dic2.items())

    diclis1 = sorted(diclis1, key = lambda x:x[1], reverse=True)
    diclis2 = sorted(diclis2, key = lambda x:x[1], reverse=True)

    key1, val1 = diclis1[0][0], diclis1[0][1]
    key2, val2 = diclis2[0][0], diclis2[0][1]
    

    if key1 != key2:
        print((n- val1 - val2))
    else:
        #print(diclis1, diclis2, len(diclis1))
        if len(diclis1) > 1 and len(diclis2) > 1:
            ans = min(n-diclis1[0][1]-diclis2[1][1], n-diclis1[1][1]-diclis2[0][1])
        
        elif len(diclis2) > 1:
            ans = min(n//2 + n//2 - diclis2[1][1], n/2 - diclis2[0][1])
        elif len(diclis1) > 1:
            ans = min(n//2 + n//2 - diclis1[1][1], n/2 - diclis1[0][1])
        else:
            ans = n//2


        print(ans)
    

def __starting_point():
    main()

__starting_point()
