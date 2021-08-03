n = int(input())
s = input()
tmp, ans = 0, 0
for i in range(n + 1):
    s0 = []
    for j in range(n):
        if j < i:
            t = True
            for x in s0:
                if x == s[j]:
                    t = False
            if t:
                s0.append(s[j])
        else:
            for k in range(len(s0)):
                if s0[k] == s[j]:
                    tmp += 1
                    s0[k] = -1
    # print(i,tmp)
    tmp, ans = 0, max(ans, tmp)
print(ans)
