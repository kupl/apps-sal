import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(set(map(int, input().split()))))
n = len(a)
used = [0] * n
cnt = 0
for i in range(n):
    if not used[i]:
        used[i] = 1
        cnt += 1
        for j in range(i + 1, n):
            if a[j] % a[i] == 0:
                used[j] = 1
print(cnt)
