def solve(m, s):
    if (m, s) == (1,0):
        ret = "0 0"
    elif s > 9*m or s == 0:
        ret = "-1 -1"
    else:
        mxs = [1]+[0]*(m-1)
        mns = [1]+[0]*(m-1)
        i, j = -1, 0
        while s > 1:
            if mns[i] >= 9:
                i -= 1
            if mxs[j] >= 9:
                j += 1
            mns[i]+=1
            mxs[j]+=1
            s-=1
        ret = "".join(map(str, mns+[" "]+mxs))
    return ret

    
m, s = map(int, input().split())

print(solve(m, s))
