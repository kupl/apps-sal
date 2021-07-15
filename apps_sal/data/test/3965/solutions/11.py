n = int(input())
l = list(map(int,input().split()))
for i in range(n):
	s = input()
	s = s.replace("a","e").replace("i","e").replace("o","e").replace("u","e").replace("y","e").split("e")
	#print(s)
	if len(s)-1 != l[i]:
		print("NO")
		return
print("YES")

