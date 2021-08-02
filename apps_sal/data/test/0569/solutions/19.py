def diff_subs(inp):
    if len(inp) > 26:
        return -1
    return len(inp) - len(set(inp))


useless = input()
print(diff_subs(input().strip()))
