n = int(input())
for p in map(int, input().split()):
    line = input()
    if p != sum([line.count(c) for c in "aeiouy"]):
        print("NO")
        break
else:
    print("YES")

