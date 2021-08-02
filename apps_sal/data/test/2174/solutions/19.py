n = int(input())
a = sorted(map(int, input().split()))
print(sum([abs(a[i] - i - 1) for i in range(n)]))
