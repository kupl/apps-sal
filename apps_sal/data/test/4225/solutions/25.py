[A, B, C, K] = list(map(int, list(input().split(' '))))
left = K
ans = 0
# A
left = K - A
if(left >= 0):
    ans += A
else:
    ans += K
# B .. do nothing as diff would be 0
left = left - B
# C .. no need to subtract the left anymore
if(left > 0):
    ans -= left

print(ans)
