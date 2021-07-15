a = list(map(int, input().split()))
s = input()
print(sum([a[int(c) - 1] for c in s]))
