def doall():
    t = int(input())
    def solve(n, k, d1, d2):
        if n % 3 == 0:
            r = n - k
            a = [[0, d1, d1 + d2],
                 [0, d1, d1 - d2],
                 [0, -d1, -d1 + d2],
                 [0, -d1, -d1 - d2]]
            for now in a:
                mn = min(now)
                sumn = sum(now)
                sumb = sumn - 3 * min(now)
                if k < sumb or (k - sumb) % 3 != 0:
                    continue
                w = max(now)
                tmp = 3 * w - sumn
                if tmp <= r and (r - tmp) % 3 == 0:
                    
                    return True
        return False
    ans = []
    for i in range(t):
        n, k, d1, d2 = list(map(int, input().split()))
        if solve(n, k, d1, d2):
            ans.append('yes')
        else:
            ans.append('no')
    print('\n'.join(ans))
                
doall()
