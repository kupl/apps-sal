#https://mirucacule.hatenablog.com/entry/2020/04/27/090908
#https://drken1215.hatenablog.com/entry/2020/04/29/171300

S=str(input())[::-1]#逆順で格納
N=len(S)
counter=[0]*2019
counter[0]=1
ans=0
num,d=0,1
for c in S:
    num += int(c) * d
    num %= 2019
    d *= 10
    d %= 2019
    counter[num]+=1
for i in counter:
    ans += i*(i-1)//2
print(ans)
