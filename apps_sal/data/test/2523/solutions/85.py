s = input()
n = len(s)
change_cnt = 0
prev_length = 1
length = 1
ans = n
for i in range(n - 1):
    if s[i] != s[i + 1]:
        ans = min(max(i + 1, n - (i+1)), ans)
print(ans)
