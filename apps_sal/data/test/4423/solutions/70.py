n = int(input())
rec = []
for i in range(n):
    (a, b) = input().split()
    rec.append([a, int(b), i + 1])
rec = sorted(rec, reverse=True, key=lambda x: x[1])
rec = sorted(rec, key=lambda x: x[0])
for i in rec:
    print(i[2])
