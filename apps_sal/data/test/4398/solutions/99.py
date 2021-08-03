n = int(input())
s, t = map(str, input().split())
print(*[s[i] + t[i] for i in range(n)], sep="")
