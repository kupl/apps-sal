n = int(input())
for i in range(n + 1, 1000000000000):
    s = str(i)
    if s.count('8') != 0:
        print(i - n)
        return

