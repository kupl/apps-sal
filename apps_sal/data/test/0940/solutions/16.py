s = list(map(int, input().split()))
s.sort()
print(max(0, s[2] - s[1] - s[0] + 1))
