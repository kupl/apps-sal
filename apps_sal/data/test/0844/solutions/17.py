from collections import Counter

N = int(input())
nums = input().strip()
current_sum = 0
dict = {0: 0}
ans = 0

for i in range(1, N + 1):

    current_sum += (1 if nums[i - 1] == '1' else -1)
    if current_sum not in dict:
        dict[current_sum] = i
    else:
        l = i - dict[current_sum]
        ans = max(ans, l)
    #print(i ,current_sum,dict,ans)

print(ans)
