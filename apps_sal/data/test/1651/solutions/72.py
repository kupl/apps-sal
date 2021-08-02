s, p = map(int, input().split())
for n in range(1, 1000005):
    if n * (s - n) == p:
        print('Yes')
        return
print('No')
