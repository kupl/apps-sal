n = int(input())
lengths = list(map(int, input().split()))

if max(lengths) < sum(lengths) - max(lengths):
    print("Yes")
else:
    print("No")

