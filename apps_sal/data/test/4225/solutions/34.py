a, b, c, k = input().split(" ")

if int(k) > int(a):
    num = int(a) * 1
else:
    num = int(k) * 1

if int(k) - (int(a) + int(b)) > 0:
    num += (int(k) - int(a) - int(b)) * (-1)
else:
    num = num

print(num)
