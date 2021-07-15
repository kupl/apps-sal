n = int(input())
s = input()
a = [0] * 1000
for c in s:
    a[ord(c)] += 1
if max(a) > 1 or n == 1:
    print("Yes")
else:
    print("No")


