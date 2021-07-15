s = list(input())
m = len(s)//2
cnt = 0
for num in range(m):
    if s[num] != s[-1 + (-1*num)]:
        cnt += 1
print(cnt)
