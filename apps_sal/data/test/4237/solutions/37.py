import math
(A, B, C, D) = list(map(int, input().split()))
nad = B // D
nac = B // C
nid = (A - 1) // D
nic = (A - 1) // C
nacd = B // (D * C // math.gcd(D, C))
nicd = (A - 1) // (D * C // math.gcd(D, C))
ans = B - A + 1 - (nad - nid) - (nac - nic) + (nacd - nicd)
print(int(ans))
