n = int(input())
www = [input() for _ in range(n)]
ans = 'Yes'
if len(list(set(www))) != n:
    ans = 'No'
else:
    for i in range(1, n):
        if www[i][0] != www[i - 1][-1]:
            ans = 'No'
print(ans)
