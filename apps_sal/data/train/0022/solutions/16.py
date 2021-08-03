import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a1, k = map(int, input().split())
    a = a1
    k -= 1
    while k and str(a).count("0") == 0:
        ls = [int(str(a)[i]) for i in range(len(str(a)))]
        a += max(ls) * min(ls)
        k -= 1
    print(a)
