N = int(input())
p = list((int(input()) for i in range(N)))
print(sum(p) - max(p) // 2)
