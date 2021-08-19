n = int(input())
(d, x) = map(int, input().split())
print(sum([(d - 1) // int(input()) + 1 for _ in range(n)]) + x)
