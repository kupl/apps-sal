n = int(input())
p = [int(input()) for i in range(n)]

# 一番高いものは半額
print(sum(p)-max(p)//2)
