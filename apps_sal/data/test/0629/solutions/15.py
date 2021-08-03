n = int(input())
f = [0] + list(map(int, input().split()))
s = list(map(int, input().split())) + [0]
a = list(map(int, input().split()))
l = sorted([sum(f[:i + 1]) + a[i] + sum(s[i:]) for i in range(n)])
print(l[0] + l[1])
