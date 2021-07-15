from collections import deque
n, s, D, R = int(input()), input(), deque(), deque()
for i in range(n):
    if s[i] == "D":
        D.append(i)
    else:
        R.append(i)
while len(D) and len(R):
    if D[0] < R[0]:
        D.append(D.popleft() + n)
        R.popleft()
    else:
        R.append(R.popleft() + n)
        D.popleft()
if len(D):
    print("D")
else:
    print("R")
