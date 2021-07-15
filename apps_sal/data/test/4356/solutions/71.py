n,m = map(int, input().split())
a = [input() for i in range(n)]
b = [input() for j in range(m)]
res = "No"

if m == 1:
    for i in a:
        if b[0] in i:
            res = "Yes"
else:
    for k in range(n-m+1): # (0,1) ※aの長さを上限にbが縦に移動できる範囲
        if b[0] in a[k]: # もしa[0]かa[1]にb[0]が含まれるなら
            for l in range(n-m+1): # (0,1) ※aの長さを上限にbが横に移動できる範囲
                if b[0] == a[k][l:m+l]: # もし、b[0]がa[0/1][0:2]かa[0/1][1:3]と一致するなら
                    cnt = 0
                    for o in range(m-1): # (0,1) b[0]は一したのでそれ以外
                        if b[o+1] == a[k+o+1][l:m+l]: # b[1/2]がa[]
                            cnt += 1
                    if cnt == m-1:
                        res = "Yes"
        
print(res)
