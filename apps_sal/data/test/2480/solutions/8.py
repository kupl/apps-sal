def shaku(K,lists):
    ans=0
    SUMS=0
    index=0
    for  l  in range(len(lists)):
        while index < l or index< len(lists) and SUMS +lists[index] < K:
            SUMS += lists[index]
            index+= 1
        ans += index-l
        SUMS -= lists[l]

    return ans


n,k=map(int,input().split())
lists=list(map(int,input().split()))

uselist=[0 for i in range(n+1)]
for i in range(n):
    uselist[i+1]=(uselist[i]+lists[i])
anslist=[0 for i in range(n+1)]
for j in range(1,n+1):
    anslist[j]=(uselist[j]-j)%k
dic={}
for i in range(n+1):
    if anslist[i] in  dic.keys():
        dic[anslist[i]].append(i+1)
    else:
        dic[anslist[i]]=[1+i]
#answerに答えを格納することにする
answer=0
for lis in dic.values(): 
    sublis=[lis[0]]
    for a in range(1,len(lis)):
        sublis.append(lis[a]-lis[a-1])
    P=shaku(k,sublis)

    for some in lis:
      if some<k:
        answer-=1
    answer+=P
print(answer)
