n = int(input().strip())
x = list(map(int, input().strip().split()))

def check(y):
    for i in range(len(y)-1):
        if abs(y[i]-y[i+1]) > 1:
            return False
    return True

okay = True
if not check(x):
    okay = False
while len(x) > 1:
    m = max(x)
    x.remove(m)
    if not check(x):
        okay = False

print('YES' if okay else 'NO')

