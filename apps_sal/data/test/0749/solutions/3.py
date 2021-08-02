import string

s = input()


def max_dist(s, c):
    pos = [-1]
    for i, val in enumerate(s):
        if val == c:
            pos.append(i)
    pos.append(len(s))
    return max(pos[i + 1] - pos[i] for i in range(len(pos) - 1))


print(min(max_dist(s, c) for c in string.ascii_lowercase))
