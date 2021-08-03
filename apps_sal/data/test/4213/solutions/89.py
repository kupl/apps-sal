n = int(input())
a = list(map(int, input().split()))

answer = max(a) - min(a)

print(answer)
