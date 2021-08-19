import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
right = 0
xor = 0
ans = 0


def isOk(x, v):
    while x and v:
        if x & 1 and v & 1:
            return False
        x >>= 1
        v >>= 1
    return True


for left in range(N):
    while right < N and isOk(xor, A[right]):
        xor ^= A[right]
        right += 1
    ans += right - left
    if right == left:
        right += 1
    else:
        xor ^= A[left]
print(ans)
