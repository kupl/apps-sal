import sys
input = sys.stdin.readline


def compress(string):
    string = string + "#"
    n = len(string)
    begin, end, cnt = 0, 1, 1
    ans = []
    while end < n:
        if string[begin] == string[end]:
            end, cnt = end + 1, cnt + 1
        else:
            ans.append((string[begin], cnt))
            begin, end, cnt = end, end + 1, 1
    return ans


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()[:-1]
    
    s = compress(s)

    
    w_groups = 0
    w_cnt = 0
    l_cnt = 0
    li = []
    for i, (char, cnt) in enumerate(s):
        if char == "W":
            w_groups += 1
            w_cnt += cnt
        if char == "L":
            l_cnt += cnt
            if 1 <= i < len(s) - 1:
                li.append(cnt)

    if w_cnt == 0:
        print(max(min(k, l_cnt) * 2 - 1, 0))
        continue
        
    ans = w_cnt * 2 - w_groups
    ans += min(k, l_cnt) * 2

    li.sort()
    for val in li:
        if k >= val:
            ans += 1
            k -= val
    print(ans)
