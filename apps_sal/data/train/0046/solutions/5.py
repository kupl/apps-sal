t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    cnt_r = s.count("R")
    cnt_s = s.count("S")
    cnt_p = s.count("P")
    max_cnt = max(cnt_r, cnt_s, cnt_p)

    if max_cnt == cnt_r:
        print("P" * n)
    elif max_cnt == cnt_s:
        print("R" * n)
    else:
        print("S" * n)
