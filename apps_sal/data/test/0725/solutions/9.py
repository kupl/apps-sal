n, m = [int(x) for x in input().strip().split()]
color = False
for it in range(n):
    line = [x for x in input().strip().split()]
    if 'M' in line or 'Y' in line or 'C' in line:
        print("#Color")
        color = True
        break
if not color:
    print("#Black&White")
