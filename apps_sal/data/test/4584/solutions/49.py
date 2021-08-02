n = int(input())
a = list(map(int, input().split()))

emp = [0] * (n + 1)

for i in range(len(a)):
    emp[a[i]] += 1

for i in range(1, n + 1):
    print((emp[i]))
