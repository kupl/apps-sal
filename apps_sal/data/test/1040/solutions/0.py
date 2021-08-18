import sys
readline = sys.stdin.readline


N = int(readline())
S = readline().rstrip()

ans = N
stack = []

for s in S:
    if s == "f":
        stack.append(0)
    elif s == "o":
        if stack and stack[-1] == 0:
            stack[-1] = 1
        else:
            stack = []
    elif s == "x":
        if stack and stack[-1] == 1:
            stack.pop()
            ans -= 3
        else:
            stack = []
    else:
        stack = []

print(ans)
