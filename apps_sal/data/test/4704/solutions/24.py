n = int(input())
a = list(map(int, input().split()))
val = 0
l = []
s = sum(a)
hlf = s/2
for i in range(n-1):
    val += a[i]
    l.append(abs(hlf - val))

val = min(l)
print((int(val*2)))

