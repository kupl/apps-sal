# ABC 133 C
[L, R] = [int(i) for i in input().split()]
ans = 2018
if R - L >= 2018:
    ans = 0
    #print('a')
else:
    l = L%2019
    r = R%2019
    if r < l:
        ans = 0
     #   print('b')
    else:
        for i in range(l, r):
            for j in range(i+1, r+1):
                if (i*j)%2019 < ans:
                    ans = (i*j)%2019
      #              print('c')
print(ans)
