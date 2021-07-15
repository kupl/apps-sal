n = int(input())
f = sum(int(x) for x in input().split())
print(sum(1 for x in range(1, 6) if (f + x) % (n + 1) != 1))
