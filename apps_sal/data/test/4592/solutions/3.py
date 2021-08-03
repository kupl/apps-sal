from collections import deque

p = 10**9 + 7


def primelist(n):
    l = deque([2])
    stack = deque()
    t = 1
    for x in range(3, n + 1, 2):
        flag = 0
        for y in tuple(l):
            if x % y == 0:
                flag = 1
                break
        if flag == 0:
            l.append(x)
    return l


def main():
    n = int(input())
    l = primelist(n)
    ans = 1
    while l:
        q = l.pop()
        s = 0
        c = 1
        while n // (q**c):
            s += n // (q**c)
            c += 1
        ans = ans * (s + 1) % p
    print(ans)


main()
