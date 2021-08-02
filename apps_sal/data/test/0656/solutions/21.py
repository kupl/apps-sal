"""
NTC here
"""
import sys
inp = sys.stdin.readline


def input(): return inp().strip()


flush = sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**25)


def iin(): return int(input())


def lin(): return list(map(int, input().split()))

# range = xrange
# input = raw_input


def main():
    n, k = lin()
    a = lin()
    a1 = [0] * n
    for i in range(n):
        if a[i] < 0:
            a1[i] = 1
    sm = sum(a1)
    if sm > k:
        print(-1)
    else:
        sm = k - sm
        lft = []
        ch = 0
        for i in range(n):
            if a1[i]:
                if ch and i - ch:
                    lft.append([ch, i - ch, 2])
                ch = 0
            else:
                ch += 1
        ext = []
        if ch and i + 1 - ch:
            ext = [ch, 1 + i - ch, 1]
        # print(lft, ext)
        lft.sort()
        a2 = lft + ([ext] if ext else [])
        a2.sort()

        def check(a):
            if not a:
                return 0
            # print(a)
            s1 = sm
            ans = 0
            for i, j, k in a:
                if s1 < i:
                    break
                s1 -= i
                ans += k
            return ans
        if check(a2) > check(lft):
            lft = a2
        lft = lft[::-1]
        # print(sm, a1)
        # print(lft)
        while sm and lft:
            ch, i, asd = lft.pop()
            if sm < ch:
                continue
            while sm and ch and i < n:
                a1[i] = 1
                i += 1
                sm -= 1
                ch -= 1
        # print(a1)
        ans = 0
        a1 = [0] + a1
        for i in range(1, n + 1):
            if a1[i] != a1[i - 1]:
                ans += 1
        print(ans)


main()
# threading.Thread(target=main).start()
