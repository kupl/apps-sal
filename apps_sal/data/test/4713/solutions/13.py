N = int(input())
S = input()

tmp = 0
ans = 0
for i in range(N):
    if 'I' == S[i]:
        tmp += 1
    else:
        tmp -= 1
    ans = max(tmp, ans)
print(ans)
