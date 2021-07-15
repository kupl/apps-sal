n = int(input())
#a, b = map(int,input().split())
al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans = 0
dic = {}
for a in al:
    dic[a] = dic.get(a, 0)+1

for k, v in dic.items():
    if k == v:
        pass
    elif k < v:
        ans += v-k
    else:
        ans += v
print(ans)
