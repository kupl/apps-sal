s = input()
k = int(input())
if k == 1 or len(s) == 1:
    ans = list(s)[0]
else:
    ans = None
    for (i, j) in enumerate(list(s)):
        if i < k - 1:
            if j != '1':
                ans = j
                break
        elif i == k - 1:
            ans = j
            break
        else:
            continue
print(ans)
