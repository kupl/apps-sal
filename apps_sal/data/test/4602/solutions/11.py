N = input()
K = int(input())
l = input().split()
         

         
ans =0 
for i in l:
	s = int(i)
	ans += min(s,K-s)
print((ans*2))

