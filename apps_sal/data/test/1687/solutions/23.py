n = int(input())
a = list(map(int, input().split()))
c = min(a)
for r in a:
    if r % c != 0:
        print('-1')
        quit()
print(c)
