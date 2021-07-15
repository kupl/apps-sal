n=int(input())
l=[int(i)for i in input().split()]
ans = "YES"
mod= "up"
if n>1:
	for i in range(1,n):
		if l[i-1]<l[i] :
			if mod=="up":
				continue
			else:
				ans = "NO"
				break
		elif l[i-1]==l[i] :
			if (mod =="up" or mod =="same"):
				mod = "same"
			else :			
				ans = "NO"
				break
		else  :
			mod = "down"
print(ans)
