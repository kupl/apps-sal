l = list(map(int,input().split()))
n = l[0]
x = l[1]
y = l[2]
s = input()
string = s[::-1]
count = 0
for i in range(y):
	if(string[i]=="1"):
		count+=1
if(string[y]=="0"):
	count+=1
for i in range(y+1,x):
	if(string[i]=="1"):
		count+=1
print(count)
