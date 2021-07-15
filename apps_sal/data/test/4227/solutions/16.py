import itertools

n, m = list(map(int, input().split()))

#隣接行列
path=[[False]* n for _ in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    path[a][b] = True
    path[b][a] = True

ans = 0

for i in itertools.permutations(list(range(n))):
	#頂点１が始点
	if i[0]==0:
		# 生成した順列の中をさらにループ
		for j in range(n):
			# n - 1 まで続いたら条件を満たすパスが存在する
			if j == n-1:
				ans+=1
				break
			# i[j] から i[j + 1] に行くパスがなければ終了
			if not path[i[j]][i[j + 1]]:
				break
print(ans)

