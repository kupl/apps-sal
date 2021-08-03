A, B, C, D = list(map(int, input().split()))
ali = '0' * 101
bob = '0' * 101
ali = ali[:A] + '1' * (B - A) + ali[B + 1:]
bob = bob[:C] + '1' * (D - C) + bob[D + 1:]
ans = int(ali, 2) & int(bob, 2)
print((bin(ans).count('1')))
