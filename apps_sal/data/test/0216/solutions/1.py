n = int(input())
a = [int(v) for v in input().split()]

print(sum(abs(v) for v in a))

