n = int(input())
s = str(input())
i = 0
ans = ""
count = 1
while(i < n):
    ans += s[i]
    i += count
    count += 1
print(ans)
