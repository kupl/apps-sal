n, t = list(map(int, input().split()))
num = input()
idx = num.index(".")
cnt = 1
for i in range(idx + 1, n):
    if num[i] < "5":
        if 5 - int(num[i]) == 1:
            cnt += 1
        else:
            cnt = 1
    if num[i] >= "5":
        j = min(cnt, t)
        if num[i - j] != ".":
            num = num[:i - j] + str(int(num[i - j]) + 1)
        else:
            curr = 0
            while num[idx - curr - 1] == "9" and (idx - curr) != 0:
                curr += 1
            num = num[:idx - curr - 1] + str(int(num[idx - curr - 1]) + 1) + "0" * curr if curr != idx else "1" + "0" * curr
        break
print(num)
