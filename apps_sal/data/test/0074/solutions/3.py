def prime(i):
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:
            return False
    return True


x = int(input())
if prime(x):
    print(1)
    print(x)
    quit()
i = x
while not prime(i):
    i -= 2
p1000 = [i for i in range(2, 3000) if prime(i)]
rem = x - i
if rem == 2:
    print(2)
    print(2, i)
    quit()
print(3)
for jj in p1000:
    if rem - jj in p1000:
        print(i, jj, rem - jj)
        quit()
