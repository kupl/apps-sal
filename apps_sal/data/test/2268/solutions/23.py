n, m = list(map(int, input().split()))
s = input()
orig = 'abcdefghijklmnopqrstuvwxyz'
after = orig
for _ in range(m):
    xi, yi = input().split()
    after = after.translate(str.maketrans(xi + yi, yi + xi))

print(s.translate(str.maketrans(orig, after)))

