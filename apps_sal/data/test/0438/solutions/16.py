n = int(input())
ans = list()
i = 1
while 1:
    if n < i:
        break
    n -= i
    ans.append(i)
    i += 1
ans[len(ans) - 1] += n
print(len(ans))
for i in ans:
    print(i, end=' ')
