def kek(k):
    if k % 2:
        return 'L'
    else:
        return 'R'


(n, m, k) = list(map(int, input().split()))
num_of_parta = (k - 1) // 2
r = num_of_parta // m + 1
d = num_of_parta % m + 1
s = kek(k)
print(r, d, s)
