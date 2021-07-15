n, k = map(int, input().split())
nums = [input() for i in range(n)]
nums = [(nums.count(x), sorted(map(int,set(x)))) for x in set(nums)]

k_digs = list(range(0, k+1))
res = 0

for (c, x) in nums:
    if sorted(set(x) & set(k_digs)) == k_digs:
       res += c

print(res)
