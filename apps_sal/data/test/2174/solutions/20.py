a = int(input())
b = sorted(map(int, input().split()))
print(sum([abs(b[i] - i - 1)for i in range(a)]))
