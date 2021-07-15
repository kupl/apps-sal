n, s, b, k = map(int, input().split())
a = list('1' + input() + '1')
ans = []
cnt = 0
for i in range(len(a)):
    if a[i] == '0':
        cnt += 1
    else:
        cnt = 0
    if cnt == b:
        if s > 1:
            s -= 1
        else:
            ans.append(i)
        cnt = 0
print(len(ans))
for i in range(len(ans)):
    print(ans[i], end=' ')
