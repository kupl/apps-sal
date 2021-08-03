n = int(input())
a = [int(x) for x in input().split()]
time = 0
try:
    start = a.index(1)
except:
    print(0)
    return
current = a[start]
zero_in_row = 0
def f(x): return 1 if x == 1 else 0


for i in range(start, n):
    if a[i] == 1:
        time += f(zero_in_row)
        zero_in_row = 0
        time += 1
    else:
        zero_in_row += 1

print(time)
