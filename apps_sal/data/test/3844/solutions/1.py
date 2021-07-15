n = int(input())
a = [int(i) for i in input().split()]
m = [0] * (10 ** 5 + 2)
for i in a:
    m[i] += 1
for i in range(10 ** 5 + 2):
    if m[i] % 2 != 0:
        print("Conan")
        return
print("Agasa")

