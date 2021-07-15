n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

d = {}
for x in a:
    if x not in d:
        d[x] = 0
    d[x] += 1

nums = list(d.keys())
nums.sort()

l = 0
r = len(nums)-1
while l < r:
##    print(l, r, nums, d)
    if d[nums[l]] < d[nums[r]]:
        cur = nums[l]
        nxt = nums[l+1]
        full_cost = (nxt-cur)*d[cur]
        if full_cost <= k:
            d[nxt] += d[cur]
            k -= full_cost
            l+=1
        else:
            mx = k // d[cur]
            nums[l] += mx
            break      
    else:
        cur = nums[r]
        nxt = nums[r-1]
        full_cost = (cur-nxt)*d[cur]
        if full_cost <= k:
            d[nxt] += d[cur]
            k -= full_cost
            r-=1
        else:
            mx = k // d[cur]
            nums[r] -= mx
            break   

print(nums[r]-nums[l])

