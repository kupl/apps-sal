def compress(words):
    if not words:
        return ''

    def prefix(s):
        table = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while 0 < j and s[i] != s[j]:
                j = table[j - 1]
            if s[i] == s[j]:
                j += 1
                table[i] = j
        return table[-1]
    result = [*words[0]]
    for word in words[1:]:
        n = min(len(result), len(word))
        for _ in range(prefix([*word] + ['$'] + result[-n:])):
            result.pop()
        result.extend([*word])
    return ''.join(result)


def solve():
    _ = int(input())
    words = input().split()
    print(compress(words))


solve()
