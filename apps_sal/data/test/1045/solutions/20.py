n = int(input())
ts = 0
s = 0
for i in range(100):
    ts += i
    if s + ts > n:
        print(i - 1)
        break
    s += ts
