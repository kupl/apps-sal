"""tri=[False]
def knight(x0,y0,moves,a):
	nonlocal n,tri
	m=[x0,y0]
	#elif moves==0:
	elif m==a:
		tri[0]=True
	x1=x0+1
	y1=y0+1

	if x1<=n and moves>0 and not([x1,y0] in y):
		knight(x1,y0,moves-1,a)
	if y1<=n and moves>0 and not([x0,y1] in y):
		knight(x0,y1,moves-1,a)

y=[]	#list of obstacles
n=int(input())	#n*n
k=int(input())	#no of moves
o=int(input())	#obstacles
for i in range(o):
	y+=[list(map(int,input().split(" ")))]

p=int(input())	#no of values to check
for i in range(p):
	x=[]
	tri[0]=False
	c=list(map(int,input().split(" ")))
	knight(1,1,k,c)
	print(tri[0])

	"""
"\nno=input()\ntowords(no[:])\n\n\ndef assist1(no):\n\tno=int(no)\n\n\tif no==1:\n\t\tto_add='one'\n\telif no==2:\n\t\tto_add='two'\n\telif no==3:\n\t\tto_add='three'\n\telif no==4:\n\t\tto_add='four'\n\telif no==5:\n\t\tto_add='five'\n\telif no==6:\n\t\tto_add='six'\n\telif no==7:\n\t\tto_add='seven'\n\telif no==8:\n\t\tto_add='eight'\n\telif no==9:\n\t\tto_add='nine'\n\telse:\n\t\tto_add=''\n\ndef assist2(no):\n\tbelow_hundred=int(no)\n\n\t\n\tif below_hundred==10:\n\t\tto_add='ten'\n\telif below_hundred==20:\n\t\tto_add='twenty'\n\telif below_hundred==30:\n\t\tto_add='thirty'\n\telif below_hundred==40:\n\t\tto_add='forty'\n\telif below_hundred==50:\n\t\tto_add='fifty'\n\telif below_hundred==60:\n\t\tto_add='sixty'\n\telif below_hundred==70:\n\t\tto_add='seventy'\n\telif below_hundred==80:\n\t\tto_add='eighty'\n\telif below_hundred==90:\n\t\tto_add='ninety'\n\telif below_hundred==11:\n\t\tto_add='eleven'\n\telif below_hundred==12:\n\t\tto_add='twelve'\n\telif below_hundred==13:\n\t\tto_add='thirteen'\n\telif below_hundred==14:\n\t\tto_add='fourteen'\n\telif below_hundred==15:\n\t\tto_add='felifteen'\n\telif below_hundred==16:\n\t\tto_add='sixteen'\n\telif below_hundred==17:\n\t\tto_add='seventeen'\n\telif below_hundred==18:\n\t\tto_add='eightteen'\n\telif below_hundred==19:\n\t\tto_add='nineteen'\n\telse:\n\t\tto_add=''\n\ndef towords(no):\n\n\tif 10<below_hundred<20 or below_hundred%10==0:\n\t\tassist1(no[:-2])\n\t\n\telse:\n\t\t=assist(no[-1])\n\n\tif int(no)>100:\n"
'\ndef find_sub(stri):\n\tmaxi=0\n\tif stri[0]==\'S\':\n\t\tstri=stri[stri.find(\'G\'):]\n\n\twhile True:\n\t\tif stri.find(\'G\')==-1 :\n\t\t\tbreak\n\n\t\telif stri.find(\'S\')==-1 :\n\t\t\tif len(stri)>maxi:\n\t\t\t\tmaxi=len(stri)\n\t\t\tbreak\n\n\t\tend_index=stri.find(\'S\')\n\t\tstri=stri[end_index:]\n\n\t\tif end_index > maxi:\n\t\t\tmaxi=end_index\n\n\t\tvar=stri.find(\'G\')\n\t\tif var!=-1:\n\t\t\tstri=stri[var:]\n\n\treturn maxi\n\n\t\t\t\n\n\t\t\n\ndef main():\n\tn=int(input())\n\ttrophies=input()\n\n\tif trophies.find(\'S\')==-1:\n\t\treturn n\n\tif trophies.find(\'G\')==-1:\n\t\treturn 0\n\n\n\tmaxy=0\n\tfor i in range(n):\n\t\tfor j in range(i+1,n):\n\t\t\tif trophies[i]!=trophies[j]:\t\t\t\n\t\t\t\ttemp=find_sub(trophies[:i]+trophies[j]+trophies[i+1:j]+trophies[i]+trophies[j+1:])\n\t\t\t\tif temp> maxy:\n\t\t\t\t\tmaxy=temp\n\n\treturn maxy\n\n#print(main())\n\nfor i in range(100000):\n\tprint("a", end="")'
'\ndef hhh():\n\tn,m=map(int,input().split())\n\tdone=[]\n\tcount=0\n\n\tA=list(map(int,input().split(" ")))\n\tB=list(map(int,input().split(" ")))\n\n\tfor i in range(m):\n\t\tdone.append(A[0]+B[i])\n\t\tprint(0,i)\n\n\n\twhile True:\n\t\tfor i in range(n):\n\t\t\tfor j in range(m):\n\t\t\t\tif(A[i]+B[j] not in done):\n\t\t\t\t\tprint(i,j)\n\t\t\t\t\tdone.append(A[i]+B[j])\n\t\t\t\t\tcount+=1\n\t\t\t\t\tif count==m+n-1:\n\t\t\t\t\t\tprint(done)\n\t\t\t\t\t\treturn\n\nhhh()\n\n\ndef Tee(N,M):\n\tif M - N>0:\n\t\ttemp=str(M - N)\n\telse:\n\t\ttemp=str(N - M)\n#\tprint(temp)\n\tif (int(temp)/2)%2!=0:\n\t\tprint("Even")\n\telse:\n\t\tprint("Odd")\n\n\t\nfor i in range(int(input())):\n\tN,M=map(str,input().split(" "))\n\tif int(N[-1])%2==0:\n\t\tN1=int(N[-1])+1\n#\t\tprint(N,N[-1],N1)\n\telse:\n\t\tN1=int(N[-1])\n#\t\tprint(N,N[-1],N1)\t\n\tif int(M[-1])%2==0:\n\t\tM1=int(M[-1])-1\n#\t\tprint(M,M[-1],M1)\n\telse:\n\t\tM1=int(M[-1])\n\tTee(N1,M1)'
'\t\nfrom copy import deepcopy\ndef rec(current,final,time):\n\tif memoization[current[0]][current[1]]!=-1 and memoization[current[0]][current[1]]+matrix[current[0]][current[1]]>memoization[][]\n\nmatrix=[]\nmemoization=[]\nR,C=map(int,input().split())\n\n\ntemp=[-1 for i in range(C)]\n\nfor i in range(R):\n\tmatrix.append(list(map(int,input().split())))\n\tmemoization.append[temp[:]]\n\nD=int(input())\ncurrent=[0,0]\nfor i in range(D):\n\tx=int(input())\n\ty=int(input())\n\trec(current,[x-1,y-1])\n\n\nN,K,w=map(int,input().split())\n\nArr=list(map(int,input().split()))\nfinalScore=0\nfor i in range(K):\n\t\n\tsumAll=0\n\tstartAll=0\n\tendAll=0\n\tstart=0\n\tsumI=0\n\n\tfor j in range(N):\n\t\tif(j<w):\n\t\t\tstart=0\n\t\t\tsumI+=Arr[j]\n\t\telse:\n\t\t\tstart=j-w+1\n\t\t\tsumI+=(Arr[j]-Arr[j-w])\n\n\t\tif(sumI>sumAll):\n\t\t\tsumAll=sumI\n\t\t\tstartAll=start\n\t\t\tendAll=j\n\n\tfor j in range(N-w,N):\n\t\tsumI-=Arr[j]\n\t\tstart=j+1\n\n\t\tif(sumI>sumAll):\n\t\t\tsumAll=sumI\n\t\t\tstartAll=start\n\t\t\tendAll=N-1\n\tprint(startAll,endAll)\n\tfor q in range(startAll,endAll+1):\n\t\tArr[q]=0\n\tprint(Arr)\n\tfinalScore+=sumAll\n\nprint(finalScore)\nclass div(object):\n\n\tdef __init__(self,no5,no2):\n\t\tself.no2 = no2\n\t\tself.no5 = no5\n\n\tdef __add__(self,toadd):\n\t\treturn(div(self.no5+toadd.no5,self.no2+toadd.no2))\n\t\na=[]\nans=[[]]\npath=[[]]\n\ndef rec(divObj,i,j,N,pathi):\n\tzeros=min(divObj.no5,divObj.no2)\n\n\tif ans[i][j]!=-1 and zeros<ans[i][j]:\n\t\tans[i][j]=zeros\n\t\tpath[i][j]=pathi\n\telif ans[i][j]==-1:\n\t\tans[i][j]=zeros\n\t\tpath[i][j]=pathi\n\telse:\n\t\treturn\n\n\tif j+1<N:\n\t\trec(divObj+a[i][j+1],i,j+1,N,pathi+"R")\n\n\tif i+1<N:\n\t\trec(divObj+a[i+1][j],i+1,j,N,pathi+"D")\n\nN=int(input())\n\nfor i in range(N):\n\ta.append(list(map(int,input().split())))\n\nfor i in range(N):\n\tfor j in range(N):\n\t\ttemp=a[i][j]\n\n\t\ta[i][j]=div(0,0)\n\n\t\tbr1=temp\n\n\t\twhile True:\n\t\t\tbr1=br1/5\n\t\t\tif br1%1==0:\n\t\t\t\ta[i][j].no5+=1\n\t\t\telse:\n\t\t\t\tbreak\n\n\t\tbr2=temp\n\n\t\twhile True:\n\t\t\tbr2=br2/2\n\t\t\tif br2%1==0:\n\t\t\t\ta[i][j].no2+=1\n\t\t\telse:\n\t\t\t\tbreak\n\nans = [[-1 for i in range(N)] for j in range(N)]\npath = [["" for i in range(N)] for j in range(N)]\n\nrec(a[0][0],0,0,N,"")\n\nprint(ans[N-1][N-1])\nprint(path[N-1][N-1])'
dicti = {}
for i in range(26):
    dicti[chr(97 + i)] = i + 1
k = int(input())
str1 = list(input())
str2 = list(input())
delta = []
for i in range(k):
    str1[i] = dicti[str1[i]]
    str2[i] = dicti[str2[i]]
    delta.append(str2[i] - str1[i])
for i in range(k - 1, 0, -1):
    if delta[i] < 0:
        delta[i - 1] -= 1
        delta[i] += 26
divide = []
for i in range(k - 1):
    divide.append(delta[i])
    if delta[i] % 2 != 0:
        divide[i] = delta[i] // 2
        delta[i + 1] += 26
    else:
        divide[i] = delta[i] // 2
divide.append(delta[-1] // 2)
ans = [0 for i in range(k)]
for i in range(k - 1, -1, -1):
    sumi = str1[i] + divide[i]
    if sumi > 26:
        sumi -= 26
        if i != 0:
            divide[i - 1] += 1
    ans[i] = chr(96 + sumi)
print(*ans, sep='')
