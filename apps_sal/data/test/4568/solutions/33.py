n = int(input())
s = input()
ans = []
for i in range(1,n):
    cnt = 0
    A = set(s[:i])
    B = set(s[i:])
    for j in A:
        if j in B:
            cnt += 1
    ans.append(cnt)
print(max(ans))
