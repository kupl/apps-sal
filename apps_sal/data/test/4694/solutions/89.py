N = int(input())
a = list(map(int, input().split()))
descending_a = sorted(a, reverse=True)
print(descending_a[0] - descending_a[-1])
