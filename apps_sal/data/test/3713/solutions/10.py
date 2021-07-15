n = int(input())
a = input()
ans = min(n, 3 + a.count('01') + a.count('10'))

print(ans)
