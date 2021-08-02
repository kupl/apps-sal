import sys
n = int(sys.stdin.readline())
ans = ""
diff = 0
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if(diff + x <= 500):
        ans += "A"
        diff += x
    else:
        ans += "G"
        diff -= y
if(abs(diff) <= 500):
    sys.stdout.write(ans)
else:
    print('-1')
