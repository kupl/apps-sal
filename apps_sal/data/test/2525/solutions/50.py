S = input()
Q = int(input())
query = [input().split() for _ in range(Q)]

switch = 1
top = []
bottom = []

for i in range(Q):
    if query[i][0] == "1":
        switch *= -1

    else:
        f = query[i][1]
        c = query[i][2]
        if switch == 1:
            if f == "1":
                top.append(c)
            else:
                bottom.append(c)
        else:
            if f == "1":
                bottom.append(c)
            else:
                top.append(c)

if switch == 1:
    ans = top[::-1] + list(S) + bottom
else:
    ans = bottom[::-1] + list(S)[::-1] + top

print("".join(ans))
