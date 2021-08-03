N, M = list(map(int, input().split()))
S = input()

p = N
prev = N
flag = True
ans = []
for i in range(N, -1, -1):
    if (prev - i) > M:
        ans.append(prev - p)
        prev = p
        if (prev - i) > M:
            flag = False
            break
    if S[i] == "0":
        p = i
ans.append(prev)
if flag:
    print((" ".join(map(str, ans[::-1]))))
else:
    print((-1))
