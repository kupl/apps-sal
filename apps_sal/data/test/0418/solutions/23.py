for _ in range(int(input())):
    name, before, after = input().split()
    before = int(before)
    after = int(after)
    if 2400 <= before < after:
        print("YES")
        return

print("NO")
