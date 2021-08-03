# Anything is possible when you are inner peace. Master Shifu (Kung Fun Panda)
# by : Blue Edge - Create some chaos

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(["YES", "NO"][sum(a) != m])
