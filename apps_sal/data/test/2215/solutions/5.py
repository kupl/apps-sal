inp = [int(i)for i in input().split()]
n, m = inp

for i in range(m):
    a = input()

print(('01' * (n // 2 + 1))[:n])
