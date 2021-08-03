def get(k, a, b):
    if a < k:
        return -1
    a -= k
    b -= b % k
    part_b = b // k
    if ((a % k) != 0) > part_b:
        return -1
    return part_b + a // k + 1


k, a, b = list(map(int, input().split()))

print(max(get(k, a, b), get(k, b, a)))
