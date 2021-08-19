def getPossibleSuffixes(s):
    if len(s) == 5:
        print(0)
        return
    possible_suffixes = s[5:len(s)]
    suffixes = []
    helper_hash = {}
    suffix_starts = [0 for x in range(len(possible_suffixes))]
    prev_2 = ['' for x in range(len(possible_suffixes))]
    suffix_starts[-1] = 1
    for i in range(len(possible_suffixes) - 2, -1, -1):
        if suffix_starts[i + 1] and prev_2[i + 1] != possible_suffixes[i:i + 2]:
            if not helper_hash.get(possible_suffixes[i:i + 2]):
                suffixes.append(possible_suffixes[i:i + 2])
                helper_hash[possible_suffixes[i:i + 2]] = True
            if i - 1 >= 0:
                prev_2[i - 1] = possible_suffixes[i:i + 2]
                suffix_starts[i - 1] = 1
        if i + 2 < len(possible_suffixes) and suffix_starts[i + 2] and (prev_2[i + 2] != possible_suffixes[i:i + 3]):
            if not helper_hash.get(possible_suffixes[i:i + 3]):
                suffixes.append(possible_suffixes[i:i + 3])
                helper_hash[possible_suffixes[i:i + 3]] = True
            if i - 1 >= 0:
                if prev_2[i - 1] != '':
                    prev_2[i - 1] = ''
                else:
                    prev_2[i - 1] = possible_suffixes[i:i + 3]
                suffix_starts[i - 1] = 1
    print(len(suffixes))
    suffixes.sort()
    for suffix in suffixes:
        print(suffix)


s = input()
getPossibleSuffixes(s)
