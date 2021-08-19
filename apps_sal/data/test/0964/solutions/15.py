x1, y1, x2, y2, x3, y3 = [int(s) for s in input().split()]


def print_logos(top, bottom, h1, h2):
    top_line = ""
    if 'a' in top:
        top_line += (x1 if top['a'] else y1) * "A"
    if 'b' in top:
        top_line += (x2 if top['b'] else y2) * "B"
    if 'c' in top:
        top_line += (x3 if top['c'] else y3) * "C"

    print(len(top_line))

    for i in range(h1):
        print(top_line)

    bottom_line = ""
    if 'a' in bottom:
        bottom_line += (x1 if bottom['a'] else y1) * "A"
    if 'b' in bottom:
        bottom_line += (x2 if bottom['b'] else y2) * "B"
    if 'c' in bottom:
        bottom_line += (x3 if bottom['c'] else y3) * "C"

    for i in range(h2):
        print(bottom_line)


done = False

for a in [True, False]:  # flip logo 1
    if done:
        break
    for b in [True, False]:  # flip logo 2
        if done:
            break

        for c in [True, False]:  # flip logo 3
            # try 3 side-by-side
            width = (x1 if a else y1) + (x2 if b else y2) + (x3 if c else y3)
            # all heights are correct
            if width == (y1 if a else x1) and \
               width == (y2 if b else x2) and \
               width == (y3 if c else x3):
                # success!
                print_logos({'a': a, 'b': b, 'c': c}, {}, y1 if a else x1, 0)
                done = True
                break

            # otherwise, try combinations [a, b] c, [a, c] b and [b, c] a

            # [a, b], c
            width = (x1 if a else y1) + (x2 if b else y2)
            if width == (x3 if c else y3) and \
               (y1 if a else x1) == (y2 if b else x2) and \
               (y1 if a else x1) + (y3 if c else x3) == width:
                print_logos({'a': a, 'b': b}, {'c': c}, y1 if a else x1, y3 if c else x3)
                done = True
                break

            # [a, c], b
            width = (x1 if a else y1) + (x3 if c else y3)
            if width == (x2 if b else y2) and \
               (y1 if a else x1) == (y3 if c else x3) and \
               (y1 if a else x1) + (y2 if b else x2) == width:
                print_logos({'a': a, 'c': c}, {'b': b}, y1 if a else x1, y2 if b else x2)
                done = True
                break

            # [b, c], a
            width = (x3 if c else y3) + (x2 if b else y2)
            if width == (x1 if a else y1) and \
               (y3 if c else x3) == (y2 if b else x2) and \
               (y1 if a else x1) + (y3 if c else x3) == width:
                print_logos({'b': b, 'c': c}, {'a': a}, y2 if b else x2, y1 if a else x1)
                done = True
                break

if not done:
    print(-1)
