n = int(input())
l = list(map(int, input().split()))
if n % 2 == 0:
    a = l[::-2] + l[0::2]
else:
    a = l[::-2] + l[1::2]
print(*a)
