s = input()
s = s.split()
a = int(s[0])
b = int(s[1])
count = 0
while a > 1 and b > 1:
    count += a // b
    (a, b) = (b, a % b)
if a != 0 and b != 0:
    count += a
print(count)
