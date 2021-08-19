def trans(c):
    return chr(ord(c) + 1)


n, p = list(map(int, input().split()))
s = list(input())
s[n - 1] = trans(s[n - 1])  # increment the last char
i = n - 1
while i >= 0 and i < n:
    if ord(s[i]) >= ord('a') + p:
        s[i] = 'a'  # overflow make a
        i -= 1
        s[i] = trans(s[i])  # to make lexo larger ...inc the prev char #eg bc becomes ca for p=3
    elif i > 0 and s[i] == s[i - 1] or i > 1 and s[i] == s[i - 2]:
        s[i] = trans(s[i])  # a pal substring is present..inc
    else:
        i += 1  # good good..go on
else:
    print("NO" if i < 0 else "".join(s))
    # if i became n ,,we are done
    # else wwe have no ans
