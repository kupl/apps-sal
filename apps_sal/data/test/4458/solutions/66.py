N = int(input())
P_list = list(map(int, input().split()))
num_min = 2 * 10 ** 5
ans = 0
for i in P_list:
    if num_min >= i:
        num_min = i
        ans += 1
    else:
        continue
print(ans)
