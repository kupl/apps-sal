n = int(input())
a = list(map(int, input().split()))
nums = [0] * 100005
for x in a:
    nums[x] += 1
even, odd = [], []
for p in nums:
    if p % 2 == 1 and p > 1:odd.append(p)
    elif p % 2 == 0 and p > 0:even.append(p)
ans = n
for x in odd:
    ans -= x - 1
if len(even) % 2 == 1:
    ans -= 1
for x in even:
    ans -= x - 1
print(ans)
