n = int(input())
t = list(map(int, input().split())) * 2
a, b = sorted([int(x) - 1 for x in input().split()])

print(min(sum(t[a:b]), sum(t[b:a + n])))
