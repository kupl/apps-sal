s = input()
one = -1
ans = []
p = True
for i in range(0, len(s)):
    if s[i] == '0':
        if one == -1:
            ans.append([i + 1])
        else:
            ans[one].append(i + 1)
            one -= 1
    else:
        one += 1
        if one == len(ans):
            p = False
            break
        else:
            ans[one].append(i + 1)
if p == False or one != -1:
    print("-1")
else:
    print(len(ans))
    print("\n".join([str(len(sub)) + " " + " ".join(map(str, sub)) for sub in ans]))
