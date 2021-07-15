import math

n, k = list(map(int, input().strip().split()))

if k <= 2:
    if n == 2:
        print("YES")
        print("1 2")
        print("2 1")
    else:
        print("NO")
    return

if k < 700:
    pairs = 2 * math.factorial(k)/(2*math.factorial(k-2))
    if pairs < n:
        print("NO")
        return

# Possible
print("YES")
shift = 1
written = 0
for _ in range(k-1):
    for v in range(k):
        print("{} {}".format(str(v+1), str(((v+shift)%k)+1)))
        written += 1
        if written == n:
            break
    if written == n:
        break
    shift = (shift + 1)%k


