import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    candy = [int(item) for item in input().split()]
    candy.sort(reverse=True)
    total = sum(candy)
    if candy[0] <= candy[1] + candy[2]:
        print((total - total % 2) // 2)
    else:
        print(total - (candy[0] - candy[1] - candy[2]) // 2)
