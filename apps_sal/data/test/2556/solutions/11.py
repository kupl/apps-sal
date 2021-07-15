import sys
input = sys.stdin.readline

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for a , b in AB:
    c = b//a
    p1 = b%a
    ans = (c+1)**2*p1 + c**2*(a-p1)
    print(ans)
