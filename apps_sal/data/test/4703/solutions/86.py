S = input()
ans = 0
for i in range(2**(len(S) - 1)):
    ls = []
    index = 0
    for j in range(len(S) - 1):
        if ((i >> j) & 1):
            ls.append(int(S[index:j + 1]))
            index = j + 1
    ls.append(int(S[index:]))
    ans += sum(ls)
print(ans)
