# miracle!!
# cannot believe!!

(l, r) = list(map(int, input().split()))

bl = (r - l).bit_length()

print((((r ^ l) >> bl) + 1 << bl) - 1)
