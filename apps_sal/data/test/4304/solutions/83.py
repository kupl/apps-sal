(a, b) = list(map(int, input().split()))
s = b - a
tall = 0
for i in range(1, s):
    tall += i
print(tall - a)
