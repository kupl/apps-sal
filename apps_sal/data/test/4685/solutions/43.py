s = list(map(int, input().split()))
k = int(input())
s.sort()
m = 1
m *= s[2] * 2 ** k
print(m + s[0] + s[1])
