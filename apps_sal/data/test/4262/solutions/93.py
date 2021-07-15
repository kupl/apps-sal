from itertools import permutations
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

x = permutations(sorted(p))
t =0
s = 0;
c =0;
for i,j in enumerate(x):
	if p == list(j):
		s = i+1
	if q== list(j):
		c = i+1;
		
		
		
print((abs(s-c)))

