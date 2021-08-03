class RollingHash(object):
    def __init__(self, S, base, mod):
        self.mod = mod
        l = len(S)

        self.hash_lst = [0] * (l + 1)
        self.pow_lst = [1] * (l + 1)

        for i in range(l):
            self.hash_lst[i + 1] = (self.hash_lst[i] * base + ord(S[i])) % mod
            self.pow_lst[i + 1] = (self.pow_lst[i] * base) % mod

    def get_hash(self, left, right):
        return (self.hash_lst[right] - self.hash_lst[left] * self.pow_lst[right - left] % self.mod) % self.mod


N = int(input())
S = input()

base = 1007
mod = pow(10, 9) + 7
rh = RollingHash(S, base, mod)

left = 0
right = N // 2

while left <= right:
    mid = (left + right) // 2

    found_hash = {}
    found = False
    for i in range(N - mid + 1):
        h = rh.get_hash(i, i + mid)

        if h not in found_hash:
            found_hash[h] = i
        else:
            if found_hash[h] <= i - mid:
                found = True
                break

    if found:
        left = mid + 1
    else:
        right = mid - 1


print(right)
