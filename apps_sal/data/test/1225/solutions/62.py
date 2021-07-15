H=int(input())
cnt=0
while H>1:
	H=H//2
	cnt+=1
print(2**(cnt+1)-1)
