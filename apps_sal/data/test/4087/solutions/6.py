a = int(input())
for i in range(a, 10000000):
    q = str(i)
    s = 0
    for j in q:
        s += ord(j) - ord('0')
    if s % 4 == 0:
        print(i)
        return
