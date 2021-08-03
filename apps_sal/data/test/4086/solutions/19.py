n = int(input())
nums = set()
arr = list(map(int, input().split()))
arr.reverse()
ans = []
for _ in arr:
    if _ not in nums:
        nums.add(_)
        ans.append(_)
ans.reverse()
print(len(ans))
print(*ans)
