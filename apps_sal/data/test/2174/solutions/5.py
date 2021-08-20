n = int(input())
t = list(map(int, input().split()))
t.sort()
print(sum((abs(t[i] - i - 1) for i in range(n))))
