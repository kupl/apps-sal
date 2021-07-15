a = list(map(int, input().split()))
k = int(input())

a.sort()
a[-1] *= 2 ** k

print((sum(a)))

