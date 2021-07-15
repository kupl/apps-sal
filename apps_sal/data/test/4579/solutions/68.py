n = int(input())
a = {}
for i in range(n):
    s = input()
    if s not in a:
        a[s] = 1
    else:
        a[s] += 1
print(len(a))
