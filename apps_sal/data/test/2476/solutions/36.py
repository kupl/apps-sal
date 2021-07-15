def main():
    from sys import stdin
    input = stdin.readline
    from collections import Counter as ct
    from bisect import bisect_left as bl

    n = int(input())
    max_a = sorted(ct(list(map(int, input().split()))).values())
    now_a = [i for i in max_a]
    m = len(max_a)
    cnt = m
    ans = 0
    ans_list = [0]*(n-m)

    for use in range(m, 1, -1):
        rest = ans
        nex = now_a[0]
        while rest:
            val = nex
            start = bl(now_a, val+1)
            nex += 1
            q = max(-1, start-1-rest, bl(max_a, now_a[start-1]+1)-1)
            for i in range(start-1, q, -1):
                now_a[i] += 1
            if now_a[start-1] == 1:
                cnt += start-1-q
            rest -= start-1-q
            if start != m:
                nex = now_a[start]
        while cnt >= use:
            ans += 1
            rest = use
            nex = now_a[-1]
            end = m
            while rest:
                val = nex
                start = bl(now_a, val)
                if start != 0:
                    nex = now_a[start-1]
                end = min(end, bl(now_a, val+1), start+rest)
                for i in range(start, end):
                    now_a[i] -= 1
                if now_a[start] == 0:
                    cnt -= end-start
                rest -= end-start
                end = start
        ans_list.append(ans)
    print(n)
    for i in ans_list[::-1]:
        print(i)


main()
