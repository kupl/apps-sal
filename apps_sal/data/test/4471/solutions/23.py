from bisect import bisect_left, bisect_right


def go():
    n = int(input())
    a = list(map(int, input().split()))
    ma = min(a)
    return 'YES' if all(((aa - ma) % 2 == 0 for aa in a)) else 'NO'


t = int(input())
for _ in range(t):
    print(go())
