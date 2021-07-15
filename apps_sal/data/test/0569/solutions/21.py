n = int(input())
s = input()
print(n - len(set(s)) if n <= 26 else -1)
