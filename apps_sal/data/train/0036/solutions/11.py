n = int(input())
a = list(map(int, input().split()))
input()
queries = list(map(int, input().split()))

ans = []
for i in range(n):
	ans += [i]*a[i]

for q in queries:
	print(ans[q-1]+1)

