"""#N=int(input())
n,k=map(int,input().split())
s=input()
L=[0]*26
#s=[int(x) for x in input().split()]
for j in range(0,len(s)):
    L[ord(s[j])-65]=L[ord(s[j])-65]+1
ans=1000000007
for j in range(0,k):
    ans=min(ans,L[j])
ans=k*ans
print(ans)"""
'import math\npre=[]\nfor i in range(0,45010):\n    pre.append(((i*(i+1))//2))\n#print(pre[:100])\nn=int(input())\nif(n==0 or n==1 or n==2):\n    print(\'No\')\nelse:\n    temp=0\n    t=pre[n]\n    pos=-1\n    for j in range(1,n+1):\n        if(math.gcd(pre[j],t-pre[j])>1):\n            temp=1\n            pos=j\n            break\n    if(temp==0):\n        print(\'No\')\n    else:\n        print(\'Yes\')\n        print(pos,end=" ")\n        for j in range(1,pos+1):\n            print(j,end=" ")\n        print(" ")\n        print(n-j,end=" ")\n        for j in range(pos+1,n+1):\n            print(j,end=" ")\n        print(" ")'
n = int(input())
s1 = [int(x) for x in input().split()]
s2 = [int(x) for x in input().split()]
S1 = sorted(s1)
S2 = sorted(s2)
S1 = [0] + S1
S2 = [0] + S2
S1 = S1[::-1]
S2 = S2[::-1]
pta = 0
ptb = 0
sm1 = 0
sm2 = 0
for j in range(0, 2 * n + 1):
    if j % 2 == 0:
        if S2[ptb] > S1[pta]:
            ptb = ptb + 1
        else:
            sm1 = sm1 + S1[pta]
            pta = pta + 1
    elif S1[pta] > S2[ptb]:
        pta = pta + 1
    else:
        sm2 = sm2 + S2[ptb]
        ptb = ptb + 1
    if pta == n + 1 and ptb == n + 1:
        break
print(sm1 - sm2)
