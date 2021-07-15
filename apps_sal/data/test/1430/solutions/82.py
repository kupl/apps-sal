n, k = list(map(int, input().split()))
s = list(map(int, input()))
cnt = 0
ans = 0
start = 0
for i in range(n):
    if s[i] == 0 and (i == 0 or s[i - 1] == 1):
        cnt += 1
    
    if cnt == k + 1:
        while True:
            start += 1
            if s[start - 1] == 0 and s[start] == 1:
                break
        cnt -= 1
    ans = max(ans, i - start + 1)

print(ans)

