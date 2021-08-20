_ = input()
a = set(map(int, input().split()))
if len(a) % 2 == 0:
    print(len(a) - 1)
else:
    print(len(a))
