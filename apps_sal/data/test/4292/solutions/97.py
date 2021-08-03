n, k = input().split()
p = [int(i) for i in input().split()]

int_k = int(k) - 1

p = sorted(p)
print((sum(p[0:int(k)])))
