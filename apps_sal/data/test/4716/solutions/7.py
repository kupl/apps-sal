a, b = list(map(int, input().split()))
final = list(map(int, input().split()))

final.sort(reverse = True)
print((sum(final[:b])))

