def needs_trailing(segment):
    open_parens = 0
    for i in segment:
        if i == '(':
            open_parens += 1
        elif i == ')' or i == '#':
            open_parens -= 1
        if open_parens < 0:
            return -1
    return open_parens


line = input()
extra_parens = needs_trailing(line)
last_segment_needs = needs_trailing(line.split('#')[-1])
if extra_parens < 0:
    print(-1)
elif last_segment_needs > 0:
    print(-1)
else:
    outputs = [1 for i in range(line.count('#'))]
    outputs[-1] += needs_trailing(line)
    new_str = line.rpartition('#')[0].replace('#', ')') + outputs[-1] * ')' + line.rpartition('#')[-1]
    if needs_trailing(new_str) != 0:
        print(-1)
    else:
        for output in outputs:
            print(output)
