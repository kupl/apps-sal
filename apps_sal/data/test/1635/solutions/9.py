n = int(input())
mas = list(map(int, input().split()))
s = dict()
for (i, e) in enumerate(mas):
    s[e] = i
print(mas[min(s.values())])
