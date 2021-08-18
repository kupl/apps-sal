N = int(input())
S = str(input())

ans = 0
count = 0
for i in S:
    if i == 'I':
        count += 1
    elif i == 'D':
        count -= 1
    ans = max(ans, count)

print(ans)
