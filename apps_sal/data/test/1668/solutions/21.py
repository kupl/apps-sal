"""
NTC here
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


def main():
    t = iin()
    while t:
        t -= 1
        n = iin()
        ans = []
        dc = set()
        ch = 0
        todo = []
        for _ in range(n):
            s = input()
            if s in dc:
                ans.append(s)
                todo.append(_)
            else:
                ans.append(s)
                dc.add(s)
        for j in todo:
            s = ans[j]
            ch += 1
            for i in range(10):
                if str(i) + s[1:] not in dc:
                    ans[j] = str(i) + s[1:]
                    dc.add(ans[j])
                    break

        print(ch)
        print(*ans, sep='\n')


main()
