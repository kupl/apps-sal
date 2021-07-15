hutamoji_list=[[None]*11 for i in range(3)]#35,37,57の順
def hutamoji(keta,one,two):
    nonlocal hutamoji_list
    if one*two==15:
        index=0
    elif one*two==21:
        index=1
    else:
        index=2
    if hutamoji_list[index][keta]!=None:
        return hutamoji_list[index][keta]
    ans=[]
    if keta==1:
        return ans
    for each in hutamoji(keta-1,one,two):
        ans.append(one*(10**(keta-1))+each)
        ans.append(two * (10 ** (keta - 1)) + each)
    for i in [one,two]:
        for j in [one,two]:
            if i!=j:
                ans.append(i*(10**(keta-1))+int(str(j)*(keta-1)))
    ans.sort()
    hutamoji_list[index][keta]=ans

    return ans


def sannmoji(keta):
    hitigosan=[3,5,7]
    ans=[]
    if keta<=2:
        return ans
    for each in sannmoji(keta-1):
        for i in [3,5,7]:
            ans.append(i*(10**(keta-1))+each)
    for one,two,three in [[3,5,7],[5,3,7],[7,3,5]]:
        hutas=hutamoji(keta-1,two,three)
        for huta in hutas:
            ans.append(one*(10**(keta-1))+huta)
    ans.sort()
    return ans


sannmoji(10)
n=input()
keta=len(n)
n=int(n)
ans=0
for i in range(1,keta):
    ans+=len(sannmoji(i))

for i in sannmoji(keta):
    if i <=n:
        ans+=1
    else:
        break
print(ans)
