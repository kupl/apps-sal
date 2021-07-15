import sys
import collections
input = sys.stdin.readline

def main():
    S = input().strip()

    a = [[] for _ in range(26)]

    for i, s in enumerate(S):
        a[ord(s) - ord('a')].append(i)

    ans = []
    f = False
    for i in range(26):
        for j in range(len(a[i]) - 1):
            if (a[i][j + 1] - a[i][j] + 1) < 4:
                ans.append(a[i][j])
                ans.append(a[i][j + 1])
                f = True
                break
        if f:
            break

    if f:
        print((ans[0] + 1, ans[1] + 1))
    else:
        print((-1, -1))







    

def __starting_point():
    main()



__starting_point()
