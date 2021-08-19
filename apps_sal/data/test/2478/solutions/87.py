from collections import deque

N = int(input())
S = input()

reserveL = deque()
out = deque()
q = deque()

for s in S:
    if s == "(":
        reserveL.append(s)
        out.append("(")
    else:
        # print(len(reserveL))
        if len(reserveL) == 0:
            out.appendleft("(")
            out.append(")")
        else:
            out.append(")")
            reserveL.popleft()

    # print(out)

# print(out)
while reserveL:
    out.append(")")
    reserveL.popleft()
ans = ""
while out:
    ans += out.popleft()
print(ans)
