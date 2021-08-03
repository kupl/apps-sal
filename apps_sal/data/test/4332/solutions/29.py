n = int(input())
ns = "{:010d}".format(n)
ns = str(ns)
sum = 0
for i in range(10):
    sum += int(ns[i])
if n % sum == 0:
    print("Yes")
else:
    print("No")
