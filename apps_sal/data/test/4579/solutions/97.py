n = int(input())
s = list((input() for _ in range(n)))
keihin = set()
for i in s:
    keihin.add(i)
print(len(keihin))
