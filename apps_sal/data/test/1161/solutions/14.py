opens = ['(', '{', '<', '[']
closes = [')', '}', '>', ']']

def solve(inp):
    stack = []
    res = 0
    for i, x in enumerate(inp):
        if x in opens:
            stack.append((i,x))
        if x in closes:
            if not stack:
                return 'Impossible'
            ii, xx = stack.pop()
            if closes.index(x) != opens.index(xx):
                res += 1
    if stack:
        return 'Impossible'
    return res

print(solve(input()))

