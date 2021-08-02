n = int(input())
a = list(map(int, input().split()))
b = [abs(i) for i in a]
print(sum(b) - sum(i < 0 for i in a) % 2 * min(b) * 2)
