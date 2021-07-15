n = int(input())

l = [''] * n

for i in range(n):
    l[i] = input()

print((len(list(set(l)))))

