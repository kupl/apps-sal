s, p = map(int, input().split())

for i in range(1, int(p**0.5)+1):
    if p % i == 0 and i + p//i == s:
        print('Yes')
        return

print('No')
