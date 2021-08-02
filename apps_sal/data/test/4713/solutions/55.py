N = int(input())
S = input()
x = 0
ans = x

for i in range(N):
    if S[i] == "I":
        x += 1
        ans = max(ans, x)
    else:
        x -= 1
print(ans)
