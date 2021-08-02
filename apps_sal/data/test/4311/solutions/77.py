s = int(input())
ans = [s]
i = 1
if s == 1 or s == 2:
    ans = 4
else:
    while ans[i - 1] != 4:
        if ans[i - 1] % 2 == 0:
            ans.append(ans[i - 1] // 2)
        else:
            ans.append(ans[i - 1] * 3 + 1)
        i += 1
    ans = i + 3
print(ans)
