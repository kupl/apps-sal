a, b = input().split()
a = int(a + b)

for i in range(1000):
    if i ** 2 == a:
        print("Yes")
        break
else:
    print("No")
