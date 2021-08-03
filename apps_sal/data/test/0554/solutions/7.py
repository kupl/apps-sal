def solve():
    n, m = list(map(int, input().split()))
    flower = list(map(int, input().split()))
    result = 0
    for _ in range(m):
        start, end = list(map(int, input().split()))
        subSum = sum(flower[start - 1:end])
        if subSum > 0:
            result += subSum
    print(result)


solve()
