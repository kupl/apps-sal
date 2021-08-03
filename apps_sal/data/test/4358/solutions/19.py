n = int(input())
p = [0] * n
for i in range(n):
    p[i] = int(input())
answer = sum(p)
answer -= max(p) // 2
print(answer)
