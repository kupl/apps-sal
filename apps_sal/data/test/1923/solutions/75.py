n = int(input())
l = list(map(int, input().split()))
l = sorted(l)
print(sum([l[2 * i] for i in range(n)]))
