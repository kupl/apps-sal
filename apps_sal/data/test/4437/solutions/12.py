n = int(input())
li = list(input())

ans = []
cnt = 0
for i in range(n // 2):
    if li[2 * i] == li[2 * i + 1]:
        if li[2 * i] == "a":
            ans.append("b")
            ans.append(li[2 * i + 1])
            cnt += 1
        if li[2 * i] == "b":
            ans.append("a")
            ans.append(li[2 * i + 1])
            cnt += 1
    else:
        ans.append(li[2 * i])
        ans.append(li[2 * i + 1])
print(cnt)
print("".join(map(str, ans)))
