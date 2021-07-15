n = int(input())
ai = list(map(int, input().split()))
ai_sort = sorted(ai, reverse=True)
alice = ai_sort[::2]
print(sum(alice) - (sum(ai) - sum(alice)))
