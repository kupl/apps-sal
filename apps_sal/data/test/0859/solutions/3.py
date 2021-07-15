import math

#input

s1=str(input())
s2=str(input())



#variables
sum1=0
sum2=0
steps=0


def prob(x,y):
	if x>y:
		return 0
	elif y==0:
		if x==0:
			return 1
		else:
			return 0
	else:
		return (prob(x-1,y-1)+prob(x+1,y-1))/2


#main
for i in range(len(s1)):
	if s1[i]=='+':
		sum1+=1
	if s1[i]=='-':
		sum1-=1
	if s2[i]=='+':
		sum2+=1
	if s2[i]=='-':
		sum2-=1
	if s2[i]=='?':
		steps+=1

end=sum2-sum1

print(prob(end,steps))
