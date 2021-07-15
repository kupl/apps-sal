n, l, r = list(map(int, input().split()))
l -= 1
r -= 1
op = 0
curn = n
while curn > 1:
    curn //= 2
    op += 1
length = 1
for i in range(op):
    length = 2 * length + 1

def get_ans(n, l, r, curl, curr):
    if l == curl and r == curr:
        return n
    length = curr - curl + 1
    mid = (curr + curl) // 2
    ans = 0
    if l < mid:
        ans += get_ans(n // 2, l, min(mid - 1, r), curl, mid - 1)
    if r > mid:
        ans += get_ans(n // 2, max(l, mid + 1), r, mid + 1, curr)
    if l <= mid and r >= mid:
        ans += n % 2
    return ans
print(get_ans(n, l, r, 0, length - 1))


