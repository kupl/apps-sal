(n, d) = [int(i) for i in input().split(' ')]
ai = [int(i) for i in input().split(' ')]
m = int(input())
if m >= n:
    print(sum(ai) - (m - n) * d)
else:
    print(sum(sorted(ai)[:m]))
