binaryKeyboard = list(input())
ans = []
for i in binaryKeyboard:
    if i == "0" or i == "1":
        ans.append(i)
    else:
        if len(ans) == 0:
            continue
        else:
            del ans[-1]
print(''.join(ans))
