a = int(input())

ar = [0 for i in range(a)]

ar = input().split(' ')

for i in range(a):
    ar[i] = int(ar[i])

print(max(ar) ^ ar[a - 1])
