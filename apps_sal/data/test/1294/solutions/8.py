TC = int(input())
for tc in range(TC):
    grps = []
    for c in input():
        if (not grps) or grps[-1][0] != c:
            grps.append([c, 1])
        else:
            grps[-1][1] += 1
    works = [False] * 26
    for c, p in grps:
        if p % 2 == 1: works[ord(c) - ord('a')] = True
    res = ''.join(chr(x + ord('a')) for x in range(26) if works[x])
    print(res)
