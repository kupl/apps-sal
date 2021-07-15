a=int(input())
sete=set()
reg=input().split()
k=int(reg[0])
for t in range(0,k):
 sete.add(int(reg[t+1]))
re=input().split()
l=int(re[0])
for s in range(0,l):
 sete.add(int(re[s+1]))
if len(sete)==a:
 print("I become the guy.")
else:
 print("Oh, my keyboard!")


