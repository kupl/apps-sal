x = int(input())
cur = 0
for i in range(0, 45000):
    cur += i
    if x <= cur:
        print(i)
        break
