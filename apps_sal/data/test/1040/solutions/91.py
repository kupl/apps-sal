length = int(input())
string = input()
ans = []
for index in range(length):
    if string[index] == "x" and len(ans) >= 2:
        if ans[len(ans) - 2] == "f" and ans[len(ans) - 1] == "o":
            ans.pop()
            ans.pop()
        else:
            ans.append(string[index])
    else:
        ans.append(string[index])
print(len(ans))
