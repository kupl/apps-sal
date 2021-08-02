n = int(input())
ai = list(map(int, input().split()))
ai.sort()
print(ai[n // 2 - (1 - n % 2)])
