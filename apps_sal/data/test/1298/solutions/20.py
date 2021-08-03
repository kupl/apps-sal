n = int(input())
l = input()
n = 0
for e in l:
    n += (int(e) << 1) - 1
print(abs(n))
