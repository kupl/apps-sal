import sys
# sys.stdin = open("#input.txt", "r")
n = int(input())
ls = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n):
	ans = min(ans,ls[i]//max(i, n-i-1))
print(ans)
