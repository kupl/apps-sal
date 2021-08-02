b = bin(int(input()))[2:]
b = b[::-1]
val = [0 for i in range(6)]
for c in range(len(b)):
    val[5 - c] = b[c]
# print(val)
# val=val[::-1]
# print(val)
l = [0, 5, 3, 2, 4, 1]
ans = [0 for i in range(6)]
for c in range(6):
    ans[c] = val[l[c]]
print(int(''.join(map(str, ans)), 2))
