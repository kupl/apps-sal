word = input()
length = len(word)

acceptable2 = [None] * length
acceptable2[0] = True
acceptable2[1] = False
acceptable2[2] = True
acceptable2[3] = False
acceptable3 = [None] * length
acceptable3[0] = True
acceptable3[1] = False
acceptable3[2] = False
acceptable3[3] = True
all_possible_suffixes = set()


def is_acceptable(suffix, rest):
    if len(suffix) == 2:
        if acceptable3[len(rest)]:
            return True
        if acceptable2[len(rest)] and not rest.startswith(suffix):
            return True
        return False

    if len(suffix) == 3:
        if acceptable2[len(rest)]:
            return True
        if acceptable3[len(rest)] and not rest.startswith(suffix):
            return True
        return False


for i in range(length - 1, 4, -1):
    root = word[:i]
    suffixes = word[i:]

    if len(suffixes) < 2:
        continue

    first = suffixes[:2]
    rest = suffixes[2:]
    if is_acceptable(first, rest):
        all_possible_suffixes.add(first)
        acceptable2[len(suffixes)] = True
    else:
        acceptable2[len(suffixes)] = False

    if len(suffixes) < 3:
        continue

    first = suffixes[:3]
    rest = suffixes[3:]
    if is_acceptable(first, rest):
        all_possible_suffixes.add(first)
        acceptable3[len(suffixes)] = True
    else:
        acceptable3[len(suffixes)] = False


print(len(all_possible_suffixes))
for s in sorted(list(all_possible_suffixes)):
    print(s)
