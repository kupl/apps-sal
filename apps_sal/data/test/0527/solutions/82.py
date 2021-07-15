s=input()
t=input()

pos=[[] for _ in range(26)]

len_s=len(s)
len_t=len(t)


for i in range(len_s):
    idx=ord(s[i])-97
    pos[idx].append(i)

ans=[]
tmp=-1
cnt=0
for i in range(len_t):
    idx=ord(t[i])-97
    if len(pos[idx])==0:
        print((-1))
        return

    if tmp<pos[idx][-1]:
        l=-1
        r = len(pos[idx]) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if pos[idx][mid] <= tmp:
                l = mid
            else:
                r=mid
        ans.append(pos[idx][r])
        tmp=pos[idx][r]
    else:
        cnt+=1
        ans.append(pos[idx][0])
        tmp=pos[idx][0]


print((cnt*len_s+ans[-1]+1))



