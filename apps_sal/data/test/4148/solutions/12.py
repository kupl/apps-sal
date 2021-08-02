n = int(input())
s = list(input())
ans = []
for e in s:
    od = ord(e) + n
    if od > 90:
        od = 64 + od - 90
    ans.append(chr(od))
print("".join(ans))
