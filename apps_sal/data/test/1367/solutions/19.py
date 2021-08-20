n = int(input())
l = list(map(int, input().split()))
ris = 0
for e in l:
    ris += e
print(int(n * (n + 1) / 2 - ris))
