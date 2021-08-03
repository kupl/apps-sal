n = int(input())
a = list(map(int, input().split()))
d = []
for i in a:
    d.append(min(i - 1, 10**6 - i))
print(max(d))
