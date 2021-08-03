n = int(input())
works = False
for _ in range(n):
    name, start, end = input().split()
    start = int(start)
    end = int(end)
    works = works or (start >= 2400 and end > start)

print("YES" if works else "NO")
