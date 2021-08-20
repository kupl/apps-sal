def good(n):
    return sum((int(c) for c in str(n))) % 4 == 0


n = int(input())
while not good(n):
    n += 1
print(n)
