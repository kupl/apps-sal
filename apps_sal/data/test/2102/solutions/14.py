import sys
import operator
import array

#-----------

def solve():
    a = (list(map(int, input().split())))

    n = int(input())

    b = (list(map(int, input().split())))

    have = [ [] ] * (n*6)
    #have = []
    arr_append = have.append
    c=0
    for i in range(0, n):
        for j in range(0, 6):
            #arr_append(( b[i] - a[j], i ))
            have[c] = ( b[i] - a[j], i )
            c+=1

    have.sort(key=operator.itemgetter(0))

    cnt = array.array('L', [0])*n

    z = n
    sz = len(have)
    ans = 999999999999
    r = 0
    
    for i in range(0, sz):
        while (r < sz) and (z > 0):
            cnt[have[r][1]] += 1
            if (cnt[have[r][1]] == 1):
                z-=1
        
            r+=1
    
        if (z > 0):
           break

        ans = min(ans, have[r - 1][0] - have[i][0]);
        cnt[have[i][1]] -= 1
        if (cnt[have[i][1]] == 0):
            z+=1
    
    print(ans)


#-----------

def main(argv):
    solve()

def __starting_point():
    main(sys.argv)

__starting_point()
