t = int(input())
for i in range(t):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    print(sum(a[:k + 1]))
