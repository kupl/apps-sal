n = int(input())
main = list(map(int, input().split()))

total = sum(main)
beg = 0
final = float('inf')
for i in range(len(main) - 1):
    beg += main[i]
    total -= main[i]
    final = min(final, abs(beg - total))

print(final)
