n = int(input())
k = int(input())
ref = 1

for i in range(n):
    if ref * 2 < ref + k:
        ref *= 2
    else:
        ref += k

print(ref)
