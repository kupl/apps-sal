n = int(input())
s = list(map(int, input().split()))
s.sort()
for i in range(n):
    print(s[i], s[2 * n - i - 1])




