
dp = [[-1]*20 for _ in range(5)]
def dfs(pos, cnt, limited, dp, nums):
	if cnt > 3:
		return 0
	if pos == -1:
		return 1
	if not limited and dp[cnt][pos] != -1:
		return dp[cnt][pos]
	upper = nums[pos] if limited else 9
	tmp = 0
	for i in range(upper + 1):
		tmp += dfs(pos - 1, cnt + (i > 0), limited&(i==upper), dp, nums)
	if not limited:
		dp[cnt][pos] = tmp
	return tmp
def classy(num):
	nums = []
	while num:
		nums.append(num % 10)
		num //= 10
	
	return dfs(len(nums) - 1, 0, 1, dp, nums)


def __starting_point():
	T = int(input())
	for _ in range(T):
		L, R = map(int, input().split())
		print(classy(R) - classy(L-1))
__starting_point()
