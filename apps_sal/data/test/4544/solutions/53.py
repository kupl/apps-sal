import sys

input = sys.stdin.readline

n = int(input())

a_list = list(map(int, input().split()))
sort_a_list = sorted(a_list)

l = 0
r = 0
ans = 0
max_ans = 0
sabun = 0
#print(sort_a_list)

while (r < n):
    #print(l,r)
    #print(ans)
    #print(sabun)
    if (sabun <= 2):
        if sort_a_list[r] - sort_a_list[l] > 2:
            l += 1
            sabun = sort_a_list[r] - sort_a_list[l]
            ans -= 1
            continue
        ans += 1
        max_ans = max(max_ans,ans)
        r += 1
        if r >= n:
            break
        sabun = sort_a_list[r] - sort_a_list[l]
        
    else:
        l += 1
        sabun = sort_a_list[r] - sort_a_list[l]
        ans -= 1
print(max_ans)
