n = int(input())
m = len(set(map(int, input().split())))
print(('YES' if n == m else 'NO'))
