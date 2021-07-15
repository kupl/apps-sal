# author:  Taichicchi
# created: 21.09.2020 20:00:43

import sys

S = input()

Q = int(input())

rev = 0

front = []
end = []

for q in range(Q):
    query = input().split()
    if query[0] == "1":
        rev = 1 - rev
    else:
        if ((rev == 0) & (query[1] == "1")) | ((rev == 1) & (query[1] == "2")):
            front.append(query[2])
        else:
            end.append(query[2])

front = "".join(front)
end = "".join(end)


if rev:
    print((end[::-1] + S[::-1] + front))
else:
    print((front[::-1] + S + end))

