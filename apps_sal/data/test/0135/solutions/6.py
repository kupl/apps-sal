import sys

#f = open('input', 'r')
f = sys.stdin

n, k = list(map(int, f.readline().split()))

ans = 'Yes'
for tk in range(1, k + 1):
    if len(set(n % (i + 1) for i in range(tk))) != tk:
        ans = 'No'
        break

print(ans)
