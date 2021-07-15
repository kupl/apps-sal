n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [a[i - 1] for i in map(int, input().split())]
b.sort(reverse = True)
s = sum(a) - sum(b)
for i in b: s += s if i < s else i
print(s)
