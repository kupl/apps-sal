from itertools import accumulate

v = ord('v')
o = ord('o')
S = [o] + [ord(s) for s in input().strip()]

stack = []
pre = None
cnt = 0
for s in S:
    if s == pre:
        cnt += 1
    else:
        pre = s
        stack.append(cnt)
        cnt = 1
stack.append(cnt)
stack = stack[1:]

LS = len(stack)
w = 0
sp = [stack[i] - 1 if i % 2 else 0 for i in range(LS)]
sr = list(accumulate(sp))
sl = list(accumulate(sp[::-1]))[::-1]
ans = 0
for i in range(0, LS, 2):
    ans += sr[i] * sl[i] * stack[i]
print(ans)
