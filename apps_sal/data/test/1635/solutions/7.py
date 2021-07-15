n = int(input())
a = list(map(int, input().split()))
times = [10 ** 9] * 10 ** 6
for i in range(n):
    times[a[i]] = i
print(times.index(min(times)))
