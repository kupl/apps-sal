nexts = {}
prevs = {}
n = int(input())
cur = input()
prevs[cur] = -1
nexts[cur] = -1
for i in range(1,n):
    x = input()
    if x in list(nexts.keys()):
        if cur!=x:
            nexts[prevs[x]]=nexts[x]
            prevs[nexts[x]]=prevs[x]
            prevs[x]=cur
            nexts[cur]=x
            nexts[x]=-1
            cur=x
    else:
        nexts[cur]=x
        prevs[x]=cur
        cur=x
        nexts[x]=-1
while prevs[cur]!=-1:
    print(cur)
    cur = prevs[cur]
print(cur)




