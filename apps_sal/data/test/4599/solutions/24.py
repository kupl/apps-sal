n = int(input())
ai = list(map(int, input().split()))
ai_sort = sorted(ai)
alice = []
for i in range(-1, -n - 1, -2):
    alice.append(ai_sort[i])
print(sum(alice) - (sum(ai) - sum(alice)))
