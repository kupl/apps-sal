t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    l.sort()
    l.reverse()
    print(sum(l[:min(k + 1, n)]))
