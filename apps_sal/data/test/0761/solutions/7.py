def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

n = ii()
a = li()
b = [abs(x) for x in a] 
if n == 1:
    ans = a[0]
elif all(x > 0 for x in a) or all(x < 0 for x in a):
    b.sort()
    ans = sum(b) - 2 * b[0]
else:
    ans = sum(b)
print(ans)

