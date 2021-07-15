def solve():
    n = int(input())
    s = input()
    stack = []
    for c in s:
        if c == 'x' and len(stack) >= 2 and stack[-1] == 'o' and stack[-2] ==  'f':
            stack.pop()
            stack.pop()
        else:
            stack.append(c)
    print((len(stack)))


solve()

