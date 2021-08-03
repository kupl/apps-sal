
import sys
# sys.stdin=open("data.txt")
input = sys.stdin.readline

n = int(input())

pie = list(map(int, input().split()))


def dp(i):
    # best result for this player
    if i >= len(pie):
        return (0, 0)
    t1, t2 = dp(i + 1)
    return (max(pie[i] + t2 - t1, t1), t2 + pie[i])


t1, t2 = dp(0)

print(t2 - t1, t1)
