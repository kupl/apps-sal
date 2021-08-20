import sys
n = int(sys.stdin.readline())
first_p = sys.stdin.readline().split()
count = 1
vmax = 0
for i in range(n - 1):
    second_p = sys.stdin.readline().split()
    if first_p[0] == second_p[0] and first_p[1] == second_p[1]:
        count += 1
    else:
        if count > vmax:
            vmax = count
        count = 1
    first_p = second_p
if count > vmax:
    vmax = count
print(vmax)
