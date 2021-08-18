s = input()
t = input()

forward = []

backward = []

rptr = 0

for i in range(len(s)):
    if rptr == len(t):
        break
    if s[i] == t[rptr]:
        forward.append(i)
        rptr += 1

rptr = len(t) - 1
for i in range(len(s) - 1, -1, -1):
    if rptr == -1:
        break
    if s[i] == t[rptr]:
        backward.append(i)
        rptr -= 1

backward = backward[::-1]
backward.append(forward[-1])

mx = max(forward[0], len(s) - 1 - backward[-2], len(s) - 1 - forward[-1], backward[0])
for i in range(len(t)):
    mx = max(mx, abs(forward[i] - backward[i + 1]) - 1)
print(mx)
