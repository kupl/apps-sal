# ABC124
# B Great Ocean View
n = int(input())
H = list(map(int, input().split()))
high = H[0]
ct = 1
for i in range(1,n):
    if high <= H[i]:
        ct += 1
        high = H[i]
print(ct)

