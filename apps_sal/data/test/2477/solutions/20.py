(N, K) = map(int, input().split())
A = list(map(int, input().split()))


def num_of_chopping(l, threshold):
    cnt = 0
    for i in l:
        cnt += -(-i // threshold) - 1
    return cnt


low = 0
high = max(A)
while low + 1 < high:
    mid = (low + high) // 2
    cnt = num_of_chopping(A, mid)
    if cnt <= K:
        high = mid
    else:
        low = mid
print(high)
