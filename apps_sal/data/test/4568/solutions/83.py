# ABC098

N = int(input())
S = input()
ans = 0
for i in range(len(S)):
    left = set(S[0:i])
    right = set(S[i:len(S)])

    ans = max(ans, len(left & right))
print(ans)
