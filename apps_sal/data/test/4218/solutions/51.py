N = int(input())
if N % 2 == 0:
    p = 0.5
else:
    p = (N + 1) / 2 / N
print(p)
