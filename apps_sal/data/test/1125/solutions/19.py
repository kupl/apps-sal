n = int(input())
a = list(map(int, input().split()))
x = 0
for i in a[2:]: x ^= i
m = (a[0] + a[1] - x) // 2
if a[0] + a[1] != x + m * 2 or m > a[0] or (x & m) != 0: print(-1); return()
l = 1 << (max(x.bit_length(), m.bit_length()) + 1)
while l > 0:
    if((x & l) != 0) and ((m | l) <= a[0]): m |= l
    l >>= 1
print(a[0] - m if m != 0else-1)
