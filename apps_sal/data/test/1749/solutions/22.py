l, a, b = list(map(int, input().split()))
before = list(map(int, input().split()))
after = list(map(int, input().split()))

if sorted(before[a - 1: b]) != sorted(after[a - 1: b]):
    print("LIE")
elif before[:a-1] != after[:a-1]:
    print("LIE")
elif before[b:] != after[b:]:
    print("LIE")
else:
    print("TRUTH")

