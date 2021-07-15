x = input()
s = sorted(list(map(int, input().split())))
print(sum(s[::2]))
