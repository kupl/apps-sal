n, k = int(input()), int(input())
print(sum([min(abs(i * 2), abs((i - k) * 2)) for i in list(map(int, input().split()))]))
