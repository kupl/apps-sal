def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    def stoidx(s):
        if s == 'AB':
            return (0, 1)
        elif s == 'BC':
            return (1, 2)
        else:
            return (0, 2)


    def answer(ans):
        print('Yes')
        for a in ans:
            print(a)

    def add_answer(x):
        if s[x[0]] > s[x[1]]:
            s[x[0]] -= 1
            s[x[1]] += 1
            ans.append(abc[x[1]])
        else:
            s[x[0]] += 1
            s[x[1]] -= 1
            ans.append(abc[x[0]])
        
    n, *s = list(map(int, input().split()))
    sl = []
    for _ in range(n):
        sl.append(stoidx(input()))
    abc = 'ABC'
    ans = []
    if sum(s) == 0:
        print('No')
        return

    elif sum(s) == 1:
        for x in sl:
            if s[x[0]] == 0 and s[x[1]] == 0:
                print('No')
                return
            add_answer(x)

    else:
        for i, x in enumerate(sl):
            if s[x[0]] == 0 and s[x[1]] == 0:
                print('No')
                return
                
            if i < n-1 and s[x[0]] == 1 and s[x[1]] == 1:
                nx = sl[i+1]
                if x != nx and sum(s)==2:
                    if x[0] in nx:
                        s[x[0]] += 1
                        s[x[1]] -= 1
                        ans.append(abc[x[0]])
                    else:
                        s[x[0]] -= 1
                        s[x[1]] += 1
                        ans.append(abc[x[1]])
                    continue
            add_answer(x)
    answer(ans)


def __starting_point():
    main()

__starting_point()
