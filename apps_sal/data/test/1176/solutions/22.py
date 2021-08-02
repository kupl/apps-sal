n = int(input())
a = list(map(int, input().split()))

s = [abs(i) for i in a]
minus = sum([1 for i in a if i < 0])
print(sum(s) if minus % 2 == 0 else sum(s) - 2 * min(s))
