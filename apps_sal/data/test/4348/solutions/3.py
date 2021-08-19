def main():
    [n, k] = map(int, input().split())
    s = input()
    char_idxs = []
    for (idx, c) in enumerate(s):
        char_idxs.append((c, idx))
    char_idxs.sort()
    char_idxs = char_idxs[k:]
    char_idxs.sort(key=lambda cidx: cidx[1])
    lst = [c for (c, idx) in char_idxs]
    print(''.join(lst))


main()
