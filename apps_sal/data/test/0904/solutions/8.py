input()
words = input().split()
ans = 0
for item in words:
    cnt = 0
    for i in item:
        if(i.isupper()):
            cnt += 1
    ans = max(ans, cnt)
print(ans)
