import sys
def input(): return sys.stdin.readline().strip()


t = int(input())
while t:
    t -= 1
    a1, k = map(int, input().split())
    while k > 1:
        k -= 1
        val = list(map(int, list(str(a1))))
        if min(val) == 0:
            break
        # print(val)
        a1 = a1 + min(val) * max(val)
    print(a1)
