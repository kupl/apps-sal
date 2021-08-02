import sys
def input(): return sys.stdin.readline().rstrip('\r\n')


for _ in range(int(input())):
    n = int(input())
    d = [0] * (26)
    fl = True
    for _ in range(n):
        s = input()
        for i in s:
            d[ord(i) - ord('a')] += 1
    for x in d:
        if x > 0 and x % n:
            fl = False
            break
    print("YES" if fl else "NO")
