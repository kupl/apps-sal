from itertools import groupby, accumulate, product, permutations, combinations
h,w,k = map(int, input().split()) 
l = [input() for i in range(h)]
ans = 0

for i in product([0,1],repeat=h):
    for j in product([0,1],repeat=w):
        Ans = 0
        for m in range(h):
            for n in range(w):
                if l[m][n] == '#' and i[m] == 1 and j[n] == 1:
                    Ans += 1
        if Ans == k:
            ans +=1

print(ans)
