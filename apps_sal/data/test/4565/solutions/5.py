N = int(input())
S = input()

cnt = S[1:].count("E")
ans = cnt

for i in range(1, N):
    if S[i - 1] == "W":
        cnt += 1
    if S[i] == "E":
        cnt -= 1
    ans = min(ans, cnt)

print(ans)
