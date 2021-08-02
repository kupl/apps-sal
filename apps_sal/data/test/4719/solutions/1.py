n = int(input())
ans = [100] * 26
for i in range(n):
    s = input()
    lst = [0] * 26
    for j in s:
        num = ord(j) - 97
        lst[num] += 1
    for k in range(26):
        ans[k] = min(ans[k], lst[k])
for l in range(26):
    if ans[l] > 0:
        print(chr(l + 97) * ans[l], end="")
