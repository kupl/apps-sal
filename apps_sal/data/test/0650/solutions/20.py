clean = "AEFHIKLMNTVWXYZ"
string = input()
sum_ = 0
for i in string:
	if i in clean:
		sum_ +=1
if(sum_ == len(string) or sum_ == 0):
	print("YES")
else:
	print("NO")
