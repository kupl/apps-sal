n = int(input())
a = list(map(int, input().split()))
a.sort()
s = a[-1] / 2
b = [[i, abs(i - s)] for i in a]
b.sort(key=lambda z: z[1])
print(a[-1], b[0][0])
