from collections import deque
D = deque()
R = deque()
n = int(input())
people = input()
for i in range(len(people)):
    if people[i] == "D":
        D.append(i)
    else:
        R.append(i)
while D and R:
    topr, topd = R.popleft(), D.popleft()
    if topr < topd:
        R.append(topr + n)
    else:
        D.append(topd + n)
if R:
    print("R")
else:
    print("D")
