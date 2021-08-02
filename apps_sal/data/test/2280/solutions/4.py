t = int(input())
for i in range(t):
    n = int(input())
    ai = list(map(int, input().split()))
    ai.sort()
    print(min(n - 2, ai[-2] - 1))
