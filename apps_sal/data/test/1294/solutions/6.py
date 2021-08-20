t = int(input())


def run_length_compress(string):
    """文字列をランレングス圧縮する
    例) string = "aabccaaabb" -> [(2, a), (1, b), (2, c), (3, a), (2, b)]
    """
    string = string + '@'
    n = len(string)
    begin = 0
    end = 1
    cnt = 1
    ans = []
    while True:
        if end >= n:
            break
        if string[begin] == string[end]:
            end += 1
            cnt += 1
        else:
            ans.append((cnt, string[begin]))
            begin = end
            end = begin + 1
            cnt = 1
    return ans


for _ in range(t):
    s = input()
    r = run_length_compress(s)
    memo = {}
    for (i, char) in r:
        if i % 2 == 1:
            memo[char] = 1
    ans = []
    for i in memo:
        ans.append(i)
    ans = sorted(ans)
    print(''.join(ans))
