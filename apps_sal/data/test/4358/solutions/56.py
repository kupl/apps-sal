N = int(input())
p = [int(input()) for i in range(N)]
answer = sum(p)
print(int(answer - max(p) * 0.5))
