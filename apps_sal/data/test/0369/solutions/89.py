ii = lambda : int(input())
mi = lambda : list(map(int,input().split()))
li = lambda : list(map(int,input().split()))

n,m = mi()
s = input()

s = s[::-1]

ans = []
ima = 0
while ima != n:
    flag = False
    for i in range(m):
        tmp = m - i
        if ima + tmp > n:
            continue
        elif s[ima+tmp] ==str(1):
            continue
        else:
            ima += tmp
            ans.append(tmp)
            flag = True
            break
    if flag == False:
        print((-1))
        return  

print((*ans[::-1]))


