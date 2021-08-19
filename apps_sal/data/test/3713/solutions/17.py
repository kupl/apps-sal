n = int(input())
a = input()
print(min(n, 3 + a.count('01') + a.count('10')))
