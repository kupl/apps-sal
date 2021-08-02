S = input()
top = 0
end = len(S) - 1
toright = True
N = int(input())
Q = [S[i] if i <= end else "" for i in range(end + 1 + N)]

for i in range(N):
    q = input().split()
    if q[0] == "1":
        toright = not toright
    else:
        if not(toright ^ (q[1] == "1")):
            Q[top - 1] = q[2]
            top -= 1
        else:
            Q[end + 1] = q[2]
            end += 1
ans = ""
# print(Q)
# print(toright)
for i in range(top, end + 1):
    ans += Q[i]
if not toright:
    ans = ans[::-1]
print(ans)
