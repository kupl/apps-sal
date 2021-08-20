N = int(input())
S = str(input())
ans = 0
tmp = 0
for i in S:
    if i == 'I':
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp -= 1
print(ans)
