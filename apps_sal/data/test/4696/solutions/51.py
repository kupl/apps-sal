
def IS(): return int(input())
def IA(): return [int(x) for x in input().split()]


a, b = IA()
print(("Odd" if (a * b) % 2 else "Even"))
