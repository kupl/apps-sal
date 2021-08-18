"""tri=[False]
def knight(x0,y0,moves,a):
	nonlocal n,tri
	m=[x0,y0]
	elif m==a:
		tri[0]=True
	x1=x0+1
	y1=y0+1

	if x1<=n and moves>0 and not([x1,y0] in y):
		knight(x1,y0,moves-1,a)
	if y1<=n and moves>0 and not([x0,y1] in y):
		knight(x0,y1,moves-1,a)

y=[]	
n=int(input())	
k=int(input())	
o=int(input())	
for i in range(o):
	y+=[list(map(int,input().split(" ")))]

p=int(input())	
for i in range(p):
	x=[]
	tri[0]=False
	c=list(map(int,input().split(" ")))
	knight(1,1,k,c)
	print(tri[0])

	"""
"""
no=input()
towords(no[:])


def assist1(no):
	no=int(no)

	if no==1:
		to_add='one'
	elif no==2:
		to_add='two'
	elif no==3:
		to_add='three'
	elif no==4:
		to_add='four'
	elif no==5:
		to_add='five'
	elif no==6:
		to_add='six'
	elif no==7:
		to_add='seven'
	elif no==8:
		to_add='eight'
	elif no==9:
		to_add='nine'
	else:
		to_add=''

def assist2(no):
	below_hundred=int(no)

	
	if below_hundred==10:
		to_add='ten'
	elif below_hundred==20:
		to_add='twenty'
	elif below_hundred==30:
		to_add='thirty'
	elif below_hundred==40:
		to_add='forty'
	elif below_hundred==50:
		to_add='fifty'
	elif below_hundred==60:
		to_add='sixty'
	elif below_hundred==70:
		to_add='seventy'
	elif below_hundred==80:
		to_add='eighty'
	elif below_hundred==90:
		to_add='ninety'
	elif below_hundred==11:
		to_add='eleven'
	elif below_hundred==12:
		to_add='twelve'
	elif below_hundred==13:
		to_add='thirteen'
	elif below_hundred==14:
		to_add='fourteen'
	elif below_hundred==15:
		to_add='felifteen'
	elif below_hundred==16:
		to_add='sixteen'
	elif below_hundred==17:
		to_add='seventeen'
	elif below_hundred==18:
		to_add='eightteen'
	elif below_hundred==19:
		to_add='nineteen'
	else:
		to_add=''

def towords(no):

	if 10<below_hundred<20 or below_hundred%10==0:
		assist1(no[:-2])
	
	else:
		=assist(no[-1])

	if int(no)>100:
"""

"""
def find_sub(stri):
	maxi=0
	if stri[0]=='S':
		stri=stri[stri.find('G'):]

	while True:
		if stri.find('G')==-1 :
			break

		elif stri.find('S')==-1 :
			if len(stri)>maxi:
				maxi=len(stri)
			break

		end_index=stri.find('S')
		stri=stri[end_index:]

		if end_index > maxi:
			maxi=end_index

		var=stri.find('G')
		if var!=-1:
			stri=stri[var:]

	return maxi

			

		

def main():
	n=int(input())
	trophies=input()

	if trophies.find('S')==-1:
		return n
	if trophies.find('G')==-1:
		return 0


	maxy=0
	for i in range(n):
		for j in range(i+1,n):
			if trophies[i]!=trophies[j]:			
				temp=find_sub(trophies[:i]+trophies[j]+trophies[i+1:j]+trophies[i]+trophies[j+1:])
				if temp> maxy:
					maxy=temp

	return maxy


for i in range(100000):
	print("a", end="")"""

"""
def hhh():
	n,m=map(int,input().split())
	done=[]
	count=0

	A=list(map(int,input().split(" ")))
	B=list(map(int,input().split(" ")))

	for i in range(m):
		done.append(A[0]+B[i])
		print(0,i)


	while True:
		for i in range(n):
			for j in range(m):
				if(A[i]+B[j] not in done):
					print(i,j)
					done.append(A[i]+B[j])
					count+=1
					if count==m+n-1:
						print(done)
						return

hhh()


def Tee(N,M):
	if M - N>0:
		temp=str(M - N)
	else:
		temp=str(N - M)
	if (int(temp)/2)%2!=0:
		print("Even")
	else:
		print("Odd")

	
for i in range(int(input())):
	N,M=map(str,input().split(" "))
	if int(N[-1])%2==0:
		N1=int(N[-1])+1
	else:
		N1=int(N[-1])
	if int(M[-1])%2==0:
		M1=int(M[-1])-1
	else:
		M1=int(M[-1])
	Tee(N1,M1)"""
"""	
from copy import deepcopy
def rec(current,final,time):
	if memoization[current[0]][current[1]]!=-1 and memoization[current[0]][current[1]]+matrix[current[0]][current[1]]>memoization[][]

matrix=[]
memoization=[]
R,C=map(int,input().split())


temp=[-1 for i in range(C)]

for i in range(R):
	matrix.append(list(map(int,input().split())))
	memoization.append[temp[:]]

D=int(input())
current=[0,0]
for i in range(D):
	x=int(input())
	y=int(input())
	rec(current,[x-1,y-1])


N,K,w=map(int,input().split())

Arr=list(map(int,input().split()))
finalScore=0
for i in range(K):
	
	sumAll=0
	startAll=0
	endAll=0
	start=0
	sumI=0

	for j in range(N):
		if(j<w):
			start=0
			sumI+=Arr[j]
		else:
			start=j-w+1
			sumI+=(Arr[j]-Arr[j-w])

		if(sumI>sumAll):
			sumAll=sumI
			startAll=start
			endAll=j

	for j in range(N-w,N):
		sumI-=Arr[j]
		start=j+1

		if(sumI>sumAll):
			sumAll=sumI
			startAll=start
			endAll=N-1
	print(startAll,endAll)
	for q in range(startAll,endAll+1):
		Arr[q]=0
	print(Arr)
	finalScore+=sumAll

print(finalScore)
class div(object):

	def __init__(self,no5,no2):
		self.no2 = no2
		self.no5 = no5

	def __add__(self,toadd):
		return(div(self.no5+toadd.no5,self.no2+toadd.no2))
	
a=[]
ans=[[]]
path=[[]]

def rec(divObj,i,j,N,pathi):
	zeros=min(divObj.no5,divObj.no2)

	if ans[i][j]!=-1 and zeros<ans[i][j]:
		ans[i][j]=zeros
		path[i][j]=pathi
	elif ans[i][j]==-1:
		ans[i][j]=zeros
		path[i][j]=pathi
	else:
		return

	if j+1<N:
		rec(divObj+a[i][j+1],i,j+1,N,pathi+"R")

	if i+1<N:
		rec(divObj+a[i+1][j],i+1,j,N,pathi+"D")

N=int(input())

for i in range(N):
	a.append(list(map(int,input().split())))

for i in range(N):
	for j in range(N):
		temp=a[i][j]

		a[i][j]=div(0,0)

		br1=temp

		while True:
			br1=br1/5
			if br1%1==0:
				a[i][j].no5+=1
			else:
				break

		br2=temp

		while True:
			br2=br2/2
			if br2%1==0:
				a[i][j].no2+=1
			else:
				break

ans = [[-1 for i in range(N)] for j in range(N)]
path = [["" for i in range(N)] for j in range(N)]

rec(a[0][0],0,0,N,"")

print(ans[N-1][N-1])
print(path[N-1][N-1])"""


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
    if(delta[i] < 0):
        delta[i - 1] -= 1
        delta[i] += 26

divide = []

for i in range(k - 1):
    divide.append(delta[i])
    if(delta[i] % 2 != 0):
        divide[i] = delta[i] // 2
        delta[i + 1] += 26
    else:
        divide[i] = delta[i] // 2

divide.append(delta[-1] // 2)

ans = [0 for i in range(k)]

for i in range(k - 1, -1, -1):
    sumi = str1[i] + divide[i]
    if(sumi > 26):
        sumi -= 26
        if(i != 0):
            divide[i - 1] += 1
    ans[i] = (chr)(96 + sumi)

print(*ans, sep="")
