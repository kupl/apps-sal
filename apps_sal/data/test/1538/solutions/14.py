n = input()
a = list(map(int, input().split()))
aa = set(a)
b = [a.count(x) for x in aa]
print(max(b))
