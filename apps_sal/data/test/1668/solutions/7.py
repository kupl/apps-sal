def run_length_compress(string):
    string.append('@')
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


t = int(input())
for _ in range(t):
    n = int(input())
    p = [input() for i in range(n)]
    set_ = set([])
    init_set = set([])
    for i in range(n):
        init_set.add(p[i])
    ans_num = 0
    ans = []
    for i in range(n):
        flag = False
        if p[i] not in set_ and p[i] in init_set:
            ans.append(p[i])
            set_.add(p[i])
            continue
        while True:
            if p[i] not in set_ and p[i] not in init_set:
                ans.append(p[i])
                set_.add(p[i])
                if flag:
                    ans_num += 1
                break
            else:
                p[i] = str((int(p[i][0]) + 1) % 10) + p[i][1:]
                flag = True
    print(ans_num)
    for i in ans:
        print(i)
