import sys
def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    A = [int(i) for i in input().split()]
    B = [0] * 100
    for a in A:
        ct = 0
        while a:
            B[ct] += a % k
            a //= k
            ct += 1
    print("YES" if max(B) <= 1 else "NO")
