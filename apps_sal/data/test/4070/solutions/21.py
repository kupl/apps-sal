n = str(hex(int(input())))[2:]
nums = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
ch = [1, 2, 0, 1, 0, 0]
ans = 0
for i in n:
    if i >= '0' and i <= '9':
        ans += nums[ord(i) - ord('0')]
    else:
        ans += ch[ord(i) - ord('a')]
print(ans)
