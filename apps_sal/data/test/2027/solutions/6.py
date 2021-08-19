3
n = int(input())
a = list(map(int, input().split()))
a.append(0)
b = [a[i] + a[i + 1] for i in range(n)]
print(' '.join(map(str, b)))
