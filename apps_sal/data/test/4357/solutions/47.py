s = list(map(int, input().split()))
s.sort(reverse=True)
print(s[0] * 10 + s[1] + s[2])
