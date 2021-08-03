n = int(input())
a = list(map(int, input().split()))
print(0 if max(a) <= 25 else max(a) - 25)
