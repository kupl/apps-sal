n = int(input())
a = list(map(int, input().split()))

ans = 1
ansc = 0

for x in a:
    i = 0
    while (x % (2 ** i) == 0):
        i += 1
    i -= 1
    if (2 ** i == ans):
        ansc += 1
    if (2 ** i > ans):
        ans = 2 ** i
        ansc = 1

print(str(ans) + ' ' + str(ansc))
