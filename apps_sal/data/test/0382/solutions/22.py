from bisect import bisect_left, bisect_right
   
def main():
    n, m, q = list(map(int, input().split(' ')))
    s = input()
    t = input()

    ps = []
    for i in range(n-m+1):
        if t == s[i:i+m]:
            ps.append(i)
    
    ans = []
    for _ in range(q):
        l, r = list(map(int, input().split(' ')))
        l, r = l - 1, r - 1
        i = bisect_left(ps, l)
        j = bisect_right(ps, r - m + 1)
        ans.append(max(j - i, 0))
    for x in ans:
        print(x)

def __starting_point():
    main()

__starting_point()
