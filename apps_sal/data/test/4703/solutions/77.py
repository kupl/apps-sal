import sys
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    s= input()
    n = len(s)
    ans = 0
    for i in range(1<<(n-1)):
        idx = [0]
        for j in range(n-1):
            if (i>>j)&1:
                idx.append(j+1)
        idx.append(n)
        for j in range(1, len(idx)):
            ans += int(s[idx[j-1]:idx[j]])
    print(ans)


def __starting_point():
    main()
__starting_point()
