n, d = map(int,input().split())
multi = list(map(int,input().split()))
multi.sort()
save = [0]*n
for i in range(n):
	j = i+1
	while (j < n and (multi[j]- multi[i])<=d):
		j+=1
	save[i] = j-i
print(n-max(save))
