S = str(input())
N = len(S)

count = 0 

saidai = 0

vernon = ['A', 'G', 'T', 'C']

for i in range (0, N):
	if vernon.count(S[i]) > 0:
		count+=1
	else:
		saidai = max(saidai, count)
		count = 0
        
saidai = max(saidai, count)
print(saidai)
