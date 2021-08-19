N = int(input())
S = input()
ans = 0
tmp = 0
for i in range(N):
    if S[i] == 'A':
        tmp = 1
    elif S[i] == 'B' and tmp == 1:
        tmp += 1
    elif S[i] == 'C' and tmp == 2:
        ans += 1
        tmp = 0
    else:
        tmp = 0
print(ans)
