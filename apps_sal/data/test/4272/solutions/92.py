N = int(input())
S = input()

ans = 0
i = 0
while i + 2 <= N - 1:
    if S[i: i + 3] == 'ABC':
        ans += 1
    i += 1

print(ans)
return
