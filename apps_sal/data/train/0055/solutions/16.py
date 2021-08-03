import sys
input = sys.stdin.readline

ans = []
for i in range(int(input())):
    n = int(input())
    ans.append(n // 2 + n % 2)

print(*ans, sep='\n')
