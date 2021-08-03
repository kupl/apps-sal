n = int(input())
p = list(int(input()) for i in range(n))


print(sum(p) - max(p) // 2)
