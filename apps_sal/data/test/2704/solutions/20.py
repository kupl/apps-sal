(n, q) = list(map(int, input().split()))
numbers = list(map(int, input().split()))
b = min(numbers)
c = max(numbers)
for _ in range(q):
    t = int(input())
    if t >= b and t <= c:
        print('Yes')
    else:
        print('No')
