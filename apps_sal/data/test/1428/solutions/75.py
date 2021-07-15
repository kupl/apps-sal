n,c=map(int,input().split())
d=[list(map(int,input().split()))for _ in range(c)]
cc=[list(map(int,input().split()))for _ in range(n)]
ans=10**15
cnt=[[0]*c for _ in range(3)]
for i in range(n):
	for j in range(n):
		cnt[(i+j)%3][cc[i][j]-1]+=1
for i in range(c):
	for j in range(c):
		for k in range(c):
			pre_ans=0
			if i==j or j==k or k==i:
				continue
			for l in range(3):
				for m in range(c):
					if l%3==0 and m!=i:
						pre_ans+=cnt[l][m]*d[m][i]
					elif l%3==1 and m!=j:
						pre_ans+=cnt[l][m]*d[m][j]
					elif l%3==2 and m!=k:
						pre_ans+=cnt[l][m]*d[m][k]
			ans=min(ans,pre_ans)
print(ans)
