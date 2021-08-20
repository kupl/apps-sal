n = int(input())
As = list(map(int, input().split()))
count = 0
for an in As:
    while an % 2 == 0:
        count += 1
        an = an / 2
print(count)
