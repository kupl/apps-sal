n = int(input()) + 1
k = sum(list(map(int, input().split())))
t = [i % n for i in range(k, k + 5)]
print(5 - t.count(0))
