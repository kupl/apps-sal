n = int(input())
#a, b = map(int,input().split())
al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
dic = {}
for ai in al:
    dic[ai] = dic.get(ai, 0)+1

edges = sorted(list(dic.items()), reverse=True)
ans = 0
partial = False
temp = 0
for tup in edges:
    e, num = tup
    if num == 1:
        continue
    elif num == 2 or num == 3:
        if partial:
            ans = temp*e
            break
        else:
            partial = True
            temp = e
    else:
        if partial:
            ans = temp*e
            break
        else:
            ans = e**2
            break
print(ans)

