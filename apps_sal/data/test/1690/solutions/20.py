"""stdin=open('input.txt')

def input():
	return stdin.readline()[:-1]"""
n = int(input())
a = list(map(int, input().split()))
a = a[::-1]
ans = a[0]
for i in range(1, n):
    if a[i] >= a[i - 1]:
        ans += max(a[i - 1] - 1, 0)
        a[i] = max(a[i - 1] - 1, 0)
    else:
        ans += a[i]
print(ans)
