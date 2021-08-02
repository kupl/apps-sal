n = int(input())
s, t = input().split()
print(*[s + t for s, t in zip(s, t)], sep="")
