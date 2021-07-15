import sys
read = sys.stdin.read
large_p = 10**9 + 7
def main():
    n = int(input())
    s1 = tuple(input())
    s2 = tuple(input())

    s = []
    cnt = 0
    while cnt < n:
        if s1[cnt] == s2[cnt]:
            s.append(1)
        else:
            s.append(2)
            cnt += 1
        cnt += 1
    if s[0] == 2:
        ans = 6
    else:
        ans = 3
    for i1 in range(1, len(s)):
        if s[i1 - 1] == 1:
            ans *= 2
        else:
            if s[i1] == 2:
                ans *= 3
        ans = ans % large_p
    print(ans)

def __starting_point():
    main()
__starting_point()
