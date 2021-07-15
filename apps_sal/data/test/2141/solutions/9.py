import sys
input = sys.stdin.readline

n = int(input())
s = ['WB' * (n // 2) + 'W' * (n % 2), 'BW' * (n // 2) + 'B' * (n % 2)]
for i in range(n):
    print(s[i % 2])

