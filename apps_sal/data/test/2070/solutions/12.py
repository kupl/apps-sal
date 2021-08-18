def main():
    from collections import defaultdict
    tr = [defaultdict(lambda: 0) for i in range(26)]
    a = list(map(int, input().split()))
    s = input()
    count = 0
    m = [0] * 26
    num = [0] * len(s)
    pos = []
    for i in range(26):
        pos.append(list())
    for i in range(len(s)):
        num[i] += a[ord(s[i]) - ord('a')]
        if i:
            num[i] += num[i - 1]
        pos[ord(s[i]) - ord('a')].append(i)
    for i in range(26):
        if len(pos[i]) > 1:
            for j in range(len(pos[i])):
                count += tr[i][num[pos[i][j] - 1]]
                tr[i][num[pos[i][j]]] += 1
    print(count)


def __starting_point():
    main()


__starting_point()
